"""
Django settings for djangogirls project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

root = os.getcwd()
cd = lambda *p: os.path.join(root, *p)
project = os.path.basename(root)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#b7&!k2cxgw5+s$%s&p#+!_8=*lo9mv-3*p0gsozvs3%myb(=k'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEV')

TEMPLATE_DEBUG = os.environ.get('DEV')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'suit',
    #'suit_redactor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'raven.contrib.django.raven_compat',
    'django_date_extensions',
    #'storages',
    'markdown_deux',

    'core'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangogirls.urls'

WSGI_APPLICATION = 'djangogirls.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}
import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='sqlite:///%s' % (os.path.abspath(os.path.join(BASE_DIR, 'db.sqlite3'))))

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates

TEMPLATE_DIRS = (
    cd('templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'core.context_processors.statistics',
)

#Custom

AUTH_USER_MODEL = 'core.User'

SUIT_CONFIG = {
    'ADMIN_NAME': 'Django Girls'
}

#MEDIA_ROOT = 'staticfiles/media'
#MEDIA_URL = '/static/media/'

# AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
#AWS_ACCESS_KEY_ID = 'AKIAIDYIUWG6Y4ZLMLGA'
#AWS_SECRET_ACCESS_KEY = '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'
#AWS_STORAGE_BUCKET_NAME = 'django-girls'

#AWS_HEADERS = {
#    'Cache-Control': 'public, max-age=86400',
#}
#AWS_QUERYSTRING_AUTH = False

#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

#STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'


#STATIC_ROOT = 'staticfiles'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = '/assets/'
STATIC_ROOT = cd('public/assets')
MEDIA_URL = '/uploads/'
MEDIA_ROOT = cd('public/uploads')


ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN')
}

try:
    from .local_settings import *
except:
    pass
