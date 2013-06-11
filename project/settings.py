import os
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.join(
    os.path.abspath(
        os.path.join(SETTINGS_DIR, os.path.pardir),
    ),
)

try:
    from settings_dev import *
except ImportError:
    from settings_prod import *

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ben Welsh', 'ben.welsh@latimes.com'),
    ('Ben Welsh', 'ben.welsh@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'latprojects@gmail.com'
EMAIL_HOST_PASSWORD = 'ch@ndl3r'
EMAIL_USE_TLS = True

ALLOWED_HOSTS = [
    'boundaries.latimes.com',
    '54.245.116.71',
    'localhost',
]
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

AWS_ACCESS_KEY_ID = 'AKIAI5GE27SBYTY3B4PQ'
AWS_SECRET_ACCESS_KEY = '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'

MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'templates', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8%-v6^jz2k48!%)h4u6^!xvi@y6wm$omlh-=&amp;t_psi%5z03ts('

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.humanize',
    'tastypie',
    'boundaryservice',
    'toolbox',
    'finder',
    'api',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_DIR, 'django.log'),
            'maxBytes': 1024*1024*5, # 5MB,
            'backupCount': 0,
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s|%(message)s'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'finder': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'boundaries': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


EXAMPLE_SCOPE = 'California'
EXAMPLE_BOUNDARY_SET = 'County'
EXAMPLE_BOUNDARY_SETS = 'Counties' # plural
EXAMPLE_BOUNDARY_SET_CODE = 'county'
EXAMPLE_BOUNDARY_SET_CODE_BIS = 'example-boundary-set-b' # "bis" is latin for "again"
EXAMPLE_BOUNDARY_SET_RESPONSE = '' # an example JSON response
EXAMPLE_BOUNDARY = 'Example Boundary'
EXAMPLE_BOUNDARY_CODE = 'example-boundary'
EXAMPLE_BOUNDARY_RESPONSE = '' # an example JSON response
EXAMPLE_PLACE = 'Downtown Los Angeles'
EXAMPLE_PLACE_LAT_LNG = '34.05246386116084,-118.24546337127686'
# The first pair of coordinates is the latitude and longitude of the southwest
# corner of the bounding box. The second pair is for the northeast corner.
EXAMPLE_PLACE_BBOX = '31.5037,-122.3272,36.1912,-112.044'
EXAMPLE_UNIT = 'kilometre'
EXAMPLE_UNIT_CODE = 'km'

MUNIN_ROOT = '/var/cache/munin/www/'

if DEBUG_TOOLBAR:
    # Debugging toolbar middleware
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    # JavaScript panels for the deveopment debugging toolbar
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    # Debug toolbar app
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': False,
    }
