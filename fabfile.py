from __future__ import with_statement
from fabric.api import *
import os
import sys
import time
import boto
from os.path import expanduser
from datetime import datetime
from boto.ec2.connection import EC2Connection
from fabric.colors import green as _green, yellow as _yellow
pwd = os.path.dirname(__file__)
sys.path.append(pwd)
from pprint import pprint

# Global vars
env.key_filename = (expanduser("~/.ec2/ben-datadesk.pem"),)
env.user = 'ubuntu'
env.known_hosts = "/tmp/tmp_known_hosts_ec2"
env.chef = '/usr/local/bin/chef-solo -c solo.rb -j node.json'
env.app_user = 'datadesk'
env.project_dir = '/apps/boundaries.latimes.com/repo/'
env.activate = "source /apps/boundaries.latimes.com/bin/activate"
env.branch = "master"
env.AWS_SECRET_ACCESS_KEY = 'ca31LpNVIibffmv3X902B0X2defPhCYIF0cMYDY5'
env.AWS_ACCESS_KEY_ID = 'AKIAJQ6NTQOSSAF7WV6Q'


def new():
    env.hosts = ("ec2-54-245-48-59.us-west-2.compute.amazonaws.com",)


def prod():
    env.hosts = ("54.245.116.71",)

#
# Bootstrapping
#

def create_server(region='us-west-2', ami='ami-1cdd532c',
    key_name='ben-datadesk', instance_type='m1.small'):
    """
    Spin up a new server on Amazon EC2.
    
    Returns the id and public address.
    
    By default, we use Ubuntu 12.04 LTS
    """
    print("Warming up...")
    conn = boto.ec2.connect_to_region(
            region,
            aws_access_key_id = env.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = env.AWS_SECRET_ACCESS_KEY,
    )
    
    print("Reserving an instance...")
    reservation = conn.run_instances(
        ami,
        key_name=key_name,
        instance_type=instance_type,
    )
    instance = reservation.instances[0]
    print('Waiting for instance to start...')
    # Check up on its status every so often
    status = instance.update()
    while status == 'pending':
        time.sleep(10)
        status = instance.update()
    if status == 'running':
        print('New instance "' + instance.id + '" accessible at ' + instance.public_dns_name)
    else:
        print('Instance status: ' + status)
    return (instance.id, instance.public_dns_name)


def install_chef():
    """
    Install all the dependencies to run a Chef cookbook
    """
    # Install dependencies
    sudo('apt-get update', pty=True)
    sudo('apt-get install -y git-core rubygems ruby ruby-dev', pty=True)
    # Screw ruby docs.
    sudo("echo 'gem: --no-ri --no-rdoc' > /root/.gemrc")
    sudo("echo 'gem: --no-ri --no-rdoc' > /home/ubuntu/.gemrc")
    # Install Chef
    sudo('gem install chef', pty=True)


def cook():
    """
    Update Chef cookbook and execute it.
    """
    sudo('mkdir -p /etc/chef')
    sudo('chown ubuntu -R /etc/chef')
    local('ssh -i %s -o "StrictHostKeyChecking no" -o "UserKnownHostsFile %s" %s@%s "touch /tmp"' % (
            env.key_filename[0],
            env.known_hosts,
            env.user,
            env.host_string
        )
    )
    local('rsync -e "ssh -i %s -o \'UserKnownHostsFile %s\'" -av ./chef/ %s@%s:/etc/chef' % (
            env.key_filename[0],
            env.known_hosts,
            env.user,
            env.host_string
        )
    )
    sudo('cd /etc/chef && %s' % env.chef, pty=True)


def bootstrap():
    """
    Pull it all together and fire up a new server.
    
    Example usage:
    
        $ fab new bootstrap
    
    """
    instance_id, public_dns = create_server()
    # We have to sleep a bit because Amazon reports the server as 'running'
    # before you can actually SSH in. 
    print "Give us a sec..."
    time.sleep(30)
    with settings(host_string=public_dns):
        install_chef()
        cook()


def restart_apache():
    """
    Restarts apache on both app servers.
    """
    sudo("/etc/init.d/apache2 reload", pty=True)


def clean():
    """
    Erases pyc files from our app code directory.
    """
    env.shell = "/bin/bash -c"
    with cd(env.project_dir):
        sudo("find . -name '*.pyc' -print0|xargs -0 rm", pty=True)


def install_requirements():
    """
    Install the Python requirements.
    """
    _venv("pip install -r requirements.txt")


def pull():
    """
    Pulls the latest code from github.
    """
    _venv("git pull origin master;")


def syncdb():
    """
    Run python manage.py syncdb over on our prod machine
    """
    _venv("python manage.py syncdb")


def collectstatic():
    """
    Roll out the latest static files
    """
    _venv("rm -rf ./static")
    _venv("python manage.py collectstatic --noinput")


def manage(cmd):
    _venv("python manage.py %s" % cmd)


def _venv(cmd):
    """
    A wrapper for running commands in our prod virturalenv
    """
    with cd(env.project_dir):
        sudo(
            "%s && %s && %s" % (env.activate, env.activate, cmd),
            user=env.app_user
        )


def deploy():
    """
    Deploy the latest code and restart everything.
    """
    pull()
    with settings(warn_only=True):
        clean()
    install_requirements()
    restart_apache()

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


def rmpyc():
    """
    Erases pyc files from current directory.

    Example usage:

        $ fab rmpyc

    """
    print("Removing .pyc files")
    with hide('everything'):
        local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)


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

