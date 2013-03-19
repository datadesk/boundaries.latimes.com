from __future__ import with_statement
from fabric.api import *
import os
import urllib
import urllib2
from datetime import datetime
from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse as dateparse

# The 'otis' machine we're deploying on
PROD = '172.24.40.21'
# The directory where the project is kept
PATH = '/apps/graphics.latimes.com/repo/'
# Database name
DATABASE = "graphics"
# How to turn on the venv
ACTIVATE = "source /apps/graphics.latimes.com/bin/activate"
env.user = 'datadesk'


def alert_the_media():
    """
    Ring the alarm!
    """
    local("curl -I http://otis.latimes.com:8008/rollout/")


@hosts(PROD)
def deploy():
    """
    Deploy the latest code to Otis and restart everything.
    
    Does not rebuild flat files or publish to S3.
    
    A full rebuild and republish of the site would be:
        
        $ fab deploy
        $ fab build
        $ fab publish
        
    """
    pull()
    with settings(warn_only=True):
        clean()
    install_requirements()
    collectstatic()
    restart_apache()
    restart_celery()
    alert_the_media()


@hosts(PROD)
def rollout():
    """
    Deploy the latest code and rebuild and publish the site to S3.
    """
    deploy()
    build()
    publish()


@hosts(PROD)
def restart_apache():
    """
    Restarts apache on both app servers.
    """
    sudo("/etc/init.d/apache2 reload", pty=True)


@hosts(PROD)
def clean():
    """
    Erases pyc files from our app code directory.
    """
    env.shell = "/bin/bash -c"
    with cd(PATH):
        sudo("find . -name '*.pyc' -print0|xargs -0 rm", pty=True)


@hosts(PROD)
def install_requirements():
    """
    Install the Python requirements.
    """
    _venv("pip install -r requirements.txt")


@hosts(PROD)
def pull():
    """
    Pulls the latest code from github.
    """
    env.shell = "/bin/bash -c"
    with cd(PATH):
        sudo("git pull origin master;", pty=True)

@hosts(PROD)
def build():
    """
    Rebuild the whole site.
    """
    _venv("python manage.py build")
    with cd(PATH):
        sudo("chown -R datadesk build")
        sudo("chgrp -R datadesk build")


@hosts(PROD)
def publish():
    """
    Sync files with S3.
    """
    _venv("python manage.py publish")


@hosts(PROD)
def syncdb():
    """
    Run python manage.py syncdb over on our prod machine
    """
    _venv("python manage.py syncdb")


@hosts(PROD)
def collectstatic():
    """
    Roll out the latest static files
    """
    _venv("rm -rf ./static")
    _venv("python manage.py collectstatic --noinput")


@hosts(PROD)
def manage(cmd):
    _venv("python manage.py %s" % cmd)


@hosts(PROD)
def _venv(cmd):
    """
    A wrapper for running commands in our prod virturalenv
    """
    env.shell = "/bin/bash -c"
    with cd(PATH):
        sudo("%s && %s" % (ACTIVATE, cmd), pty=True)


@hosts(PROD)
def restart_celery():
    """
    Restarts the celeryd task server
    """
    _venv("/etc/init.d/celeryd_graphics restart")


@hosts(PROD)
def stop_celery():
    """
    Restarts the celeryd task server
    """
    _venv("/etc/init.d/celeryd_graphics stop")


@hosts(PROD)
def kill_celery():
    sudo("ps auxww | grep celeryd | awk '{print $2}' | xargs kill -9")


@hosts(PROD)
def update_celery_daemon():
    """
    Update the celeryd init file on prod.
    """
    with settings(warn_only=True):
        _venv("/etc/init.d/celeryd_graphics stop")
    source = os.path.join(PATH, 'init.d', 'celeryd_graphics')
    target = os.path.join('/etc', 'init.d', 'celeryd_graphics')
    with settings(warn_only=True):
        sudo("rm %s" % target)
    sudo("cp %s %s" % (source, target))
    sudo("chmod +x %s" % target)
    _venv("/etc/init.d/celeryd_graphics restart")


#
# Local
#

def update_templates():
    """
    Download the latest datadesk template release and load it into the system.
    """
    local("curl -O http://databank.latimes.com/latimes-datadesk-template/latest.zip")
    local("unzip -o latest.zip")
    local("rm latest.zip")


def load_backup(date=None, db_user='postgres'):
    """
    Load the database and media backups for a particular day.
    
    If no date provided, the latest date is downloaded.
    """
    load_media(date)
    load_db(date, user=db_user)


def backup_db():
    """
    Back up the database as a cron on the production machine.
    
    Can be downloaded from databank.latimes.com
    
    This command got it load for me.

        sudo -u postgres pg_restore -Ft -d documents-2011-10-06 /home/ben/Downloads/documents-2011-10-06.tar
    """
    from datetime import date
    fname = "%s-%s.tar" % (DATABASE, str(date.today()))
    # Runs the dump command, gzips the backup, and moves it to /tmp/
    local("sudo -u postgres /usr/bin/pg_dump %s -Ft --file=/tmp/%s" % (DATABASE, fname))
    # Transfers the file from Otis to Databank
    local("scp /tmp/%s bwelsh@databank.latimes.com:/databank/webservd/dumps/graphics.latimes.com/" % fname)
    # Deletes the tmp dump
    local("sudo rm /tmp/%s" % fname)


def get_db_backup_urls():
    """
    Fetch the list of available database backups
    """
    base_url = 'http://databank.latimes.com/dumps/graphics.latimes.com/'
    soup = BeautifulSoup(urllib2.urlopen(base_url).read())
    return [base_url + i.get('href')
        for i in soup.findAll("a") if i.get('href').endswith("tar")
    ]


def get_latest_db_backup_url():
    """
    Return the url to download the most recent db backup.
    """
    date_dict = {}
    for url in get_db_backup_urls():
        file_ = url.split("/")[-1].replace("graphics-", "").replace(".tar", "")
        year, month, day = map(int, file_.split("-"))
        date_dict[datetime(year, month, day).date()] = url
    date_tuple = date_dict.items()
    date_tuple.sort(key=lambda x:x[1], reverse=True)
    return date_tuple[0][1]


def pull_latest_db():
    """
    Pull the latest database snapshot.
    """
    url = get_latest_db_backup_url()
    path = os.path.join(os.path.dirname(__file__), url.split("/")[-1])
    urllib.urlretrieve(url, path)
    return path


def pull_db(date):
    """
    Pull the database snapshot from a particular day.
    """
    url_list = get_db_backup_urls()
    for url in url_list:
        file_ = url.split("/")[-1].replace("graphics-", "").replace(".tar", "")
        if file_ == str(date.date()):
            path = os.path.join(os.path.dirname(__file__), url.split("/")[-1])
            urllib.urlretrieve(url, path)
            return path
    raise ValueError("The date you submitted does not match an existing database snapshot.")


def load_db(date=None, user='postgres', name='', drop=False):
    """
    Download the latest database snapshot and load it on your system.
    If you do not specify a date, it will pull the most recent snapshot.
    """
    # If the user doesn't provide a date pull the most recent on.
    if not date:
        path = pull_latest_db()
    else:
        path = pull_db(date=dateparse(date))
    # If the user doesn't provide one, name the database after the date
    if not name:
        name = path.split("/")[-1].replace(".tar", "")
    # If the user wants you to drop the db first, try that
    if drop:
        with settings(warn_only=True):
            local("sudo -u %s dropdb -U %s %s" % (user, user, name))
    # Create the database
    local("sudo -u %s createdb %s" % (user, name))
    # Load the snapshot
    local("sudo -u %s pg_restore -Ft -d %s %s" % (user, name, path))
    # Delete the database file
    local("rm %s" % path)
    print "Database '%s' is ready for use. Set it as your database name in settings_dev.py" % name


def get_media_backup_urls():
    """
    Fetch the list of available media backups
    """
    base_url = 'http://databank.latimes.com/dumps/graphics.latimes.com/'
    soup = BeautifulSoup(urllib2.urlopen(base_url).read())
    return [base_url + i.get('href')
        for i in soup.findAll("a") if i.get('href').endswith("zip")
    ]


def get_latest_media_backup_url():
    """
    Return the url to download the most recent media backup.
    """
    date_dict = {}
    for url in get_media_backup_urls():
        file_ = url.split("/")[-1].replace("graphics-media-", "").replace(".zip", "")
        year, month, day = map(int, file_.split("-"))
        date_dict[datetime(year, month, day).date()] = url
    date_tuple = date_dict.items()
    date_tuple.sort(key=lambda x:x[1], reverse=True)
    return date_tuple[0][1]


def pull_latest_media():
    """
    Pull the latest media snapshot.
    """
    url = get_latest_media_backup_url()
    path = os.path.join(os.path.dirname(__file__), url.split("/")[-1])
    urllib.urlretrieve(url, path)
    return path


def pull_media(date):
    """
    Pull the media snapshot from a particular day.
    """
    url_list = get_media_backup_urls()
    for url in url_list:
        file_ = url.split("/")[-1].replace("graphics-media-", "").replace(".zip", "")
        if file_ == str(date.date()):
            path = os.path.join(os.path.dirname(__file__), url.split("/")[-1])
            urllib.urlretrieve(url, path)
            return path
    raise ValueError("The date you submitted does not match an existing media snapshot.")


def load_media(date=None):
    """
    Download the latest media snapshot and load it on your system.
    
    If you do not specify a date, it will pull the most recent snapshot.
    """
    if not date:
        path = pull_latest_media()
    else:
        path = pull_media(date=dateparse(date))
    name = path.split("/")[-1].replace(".zip", "")
    local("rm -rf ./media/")
    local("unzip %s" % path)
    local("rm %s" % path)
    print "Media snapshot '%s' is ready for use." % name


def backup_media():
    """
    Back up media as a cron on the production machine.

    Can be downloaded from databank.latimes.com.
    """
    from datetime import date
    fname = "%s-media-%s.zip" % (DATABASE, str(date.today()))
    local("cd %s && sudo zip -r %s  ./media/*" % (PATH, fname))
    local("cd %s && scp ./%s bwelsh@databank.latimes.com:/databank/webservd/dumps/graphics.latimes.com/" % (PATH, fname))
    local("cd %s && sudo rm ./%s" % (PATH, fname))


def rmpyc():
    """
    Erases pyc files from current directory.

    Example usage:

        $ fab rmpyc

    """
    print("Removing .pyc files")
    with hide('everything'):
        local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)


def cl():
    """
    Fire up the Celery test server
    """
    local("python manage.py celeryd -l info --purge --settings=settings")


def rs(port=8000):
    """
    Fire up the Django test server, after cleaning out any .pyc files.

    Example usage:
    
        $ fab rs
        $ fab rs:port=9000
    
    """
    with settings(warn_only=True):
        rmpyc()
    local("python manage.py runserver 0.0.0.0:%s" % port, capture=False)


def bs(port=8000):
    """
    Fire up our custom build server, after cleaning out any .pyc files.

    Example usage:
    
        $ fab rs
        $ fab rs:port=9000
    
    """
    rmpyc()
    local("python manage.py buildserver %s" % port, capture=False)


def sh():
    """
    Fire up the Django shell, after cleaning out any .pyc files.

    Example usage:
    
        $ fab sh
    
    """
    rmpyc()
    local("python manage.py shell", capture=False)


def load():
    """
    Prints the current load values.
    
    Example usage:
    
        $ fab stage load
        $ fab prod load
        
    """
    def _set_color(load):
        """
        Sets the terminal color for an load average value depending on how 
        high it is.
        
        Accepts a string formatted floating point.

        Returns a formatted string you can print.
        """
        value = float(load)
        template = "\033[1m\x1b[%sm%s\x1b[0m\033[0m"
        if value < 1:
            # Return green
            return template % (32, value)
        elif value < 3:
            # Return yellow
            return template % (33, value)
        else:
            # Return red
            return template % (31, value)
    
    with hide('everything'):
        # Fetch the data
        uptime = run("uptime")
        # Whittle it down to only the load averages
        load = uptime.split(":")[-1]
        # Split up the load averages and apply a color code to each depending
        # on how high it is.
        one, five, fifteen = [_set_color(i.strip()) for i in load.split(',')]
        # Get the name of the host that is currently being tested
        host = env['host']
        # Combine the two things and print out the results
        output = u'%s: %s' % (host, ", ".join([one, five, fifteen]))
        print(output)

