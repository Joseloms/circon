"""
Django settings for circon project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# from registration_defaults.settings import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2_fr8#$zn5hx6)r&)d^x#qaz1hn!tt)uf0d(@68hl5y2m7suu-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = 'users.Profile'
# Application definition

INSTALLED_APPS = (

    # Configurations
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'circon.configuration.users',
    'circon.configuration.mycompany',
    'social.apps.django_app.default',
    'wkhtmltopdf',
    'import_export',
    'rest_framework',

    # Libraries
    'pure_pagination',

    # Warehouse
    'circon.warehouse.units_measures',
    'circon.warehouse.products',
    'circon.warehouse.category',
    'circon.warehouse.request',
    'dal',
    'dal_select2',

    # Purchases
    'circon.purchases.purchase',

    # Sales
    'circon.sales.sale',

    # Acounting
    'circon.accounting.accountplan',

    # Website
    'registration',
    'registration_defaults',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
)

ROOT_URLCONF = 'circon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'circon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'circon/static/circondb'),
    }
}

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'circonsoft@gmail.com'
EMAIL_HOST_PASSWORD = '181652981987'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'circon/media')
WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'

STATIC_URL = '/static/'

#  STATIC_ROOT = os.path.join(BASE_DIR, 'circon/static')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'circon/static'),)

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 10,
    'MARGIN_PAGES_DISPLAYED': 2,
}

URL_LOGIN = '/login/'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    )

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '284446488565847'
SOCIAL_AUTH_FACEBOOK_SECRET = 'bd69092264ab6f7fbb85e5f230759d3c'
