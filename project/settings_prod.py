DEBUG = False
DEVELOPMENT, PRODUCTION = False, True
DEBUG_TOOLBAR = False

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'boundaries',
        'USER': 'boundaries', 
        'PASSWORD': '&E0w#7u8#f|,v3{',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 60 * 30,
    }
}

STATIC_URL = 'https://s3-us-west-2.amazonaws.com/boundaries.latimes.com/static/'
AWS_STORAGE_BUCKET_NAME = 'boundaries.latimes.com'
AWS_BUCKET_NAME = 'boundaries.latimes.com'
WSGI_APPLICATION = 'project.wsgi_prod.application'
