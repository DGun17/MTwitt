"""
Django settings for twitter project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^=%d6*$@7xux6!f@k_r-su+70k+h5xwb4ye*)6(7mgy__u9$ho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['hidden-depths-87691.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'tweet.apps.TweetConfig',
    'registration',
    'crispy_forms',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'twitter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'twitter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twitter',
        'USER': 'twitter',
        'PASSWORD': 'usuarioadministrador',
        'HOST': '127.0.0.1',
        'PORT':'5432',
    }
}

#Configuración de base de datos para Heroku
	# Update database configuration with $DATABASE_URL.
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#Configurando archivos staticos para heroku

#definiendo la ruta del projecto

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#definiendo ruta a la cual iran los archivos estaticos cuando se ejcute collectstatics
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')


STATICFILES_DIRS=(os.path.join(PROJECT_ROOT, 'static'),)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#Configurando email
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=25
EMAIL_HOST_USER='xionwebsec@gmail.com'
EMAIL_HOST_PASSWORD='qwertyuiops'
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

#Var to emailt resets

#configurando activacion de usuario
ACCOUNT_ACTIVATION_DAYS = 1 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
SITE_ID = 1

LOGIN_REDIRECT_URL = reverse_lazy('user:index')

#configurando bootstrap a usar por cryspy
CRISPY_TEMPLATE_PACK = 'bootstrap3'

"""
Definiendo url del login para la correcta redireccion de las vistas proporcionadas por django-redux 'registration.auth_urls',
por defecto se dirigen a la ruta "accounts/login"
 """
LOGIN_URL = reverse_lazy('auth_login')
