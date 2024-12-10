"""
Django settings for student_management_system project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import dj_database_url
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
# Add this temporarily to settings.py to debug
print("Secret Key:", os.environ.get('MY_SECRET_KEY'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('MY_SECRET_KEY')  # Consider using your secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', "false") == 'True'

# ALLOWED_HOSTS = ['smswithdjango.herokuapp.com']
# Not recommended but useful in dev mode
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')


# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Apps
    'main_app.apps.MainAppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # My Middleware
    'main_app.middleware.LoginCheckMiddleWare',
]

ROOT_URLCONF = 'student_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['main_app/templates'],  # My App Templates
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

WSGI_APPLICATION = 'student_management_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        # 'USER': os.environ.get('DB_USER'),
        # 'PASSWORD': os.environ.get('DB_PASSWORD'),
        # 'HOST': os.environ.get('DB_HOST'),
        # 'PORT': os.environ.get('DB_PORT'),
    }
}

DATABASES["default"] = dj_database_url.parse(
    os.environ.get("DB_URL"), conn_max_age=600)
print("Database Configuration:", DATABASES['default'])

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTH_USER_MODEL = 'main_app.CustomUser'
AUTHENTICATION_BACKENDS = ['main_app.EmailBackend.EmailBackend']
TIME_ZONE = 'Africa/Lagos'


# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_mails")

# Email Configuration
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# DEFAULT_FROM_EMAIL = "Student Management System <admin@admin.com>"

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
