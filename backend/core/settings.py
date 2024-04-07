"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from .env import ( env, BASE_DIR )

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    # Local apps

    'core.application',
    'core.auth',
    'core.user',

    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_standardized_errors',

    'knox',

    'rest_framework_simplejwt.token_blacklist',

    # AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    'dj_rest_auth',
    'dj_rest_auth.registration',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': env.db()
}

# Caches

CACHES = {
    "default": env.cache(),
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication Backends

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Hide warnings

SILENCED_SYSTEM_CHECKS = ['auth.W004']

# Custom user model

AUTH_USER_MODEL = "core_user.User"

# Rest Framework
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'knox.auth.TokenAuthentication',

    ),
    'EXCEPTION_HANDLER': 'drf_standardized_errors.handler.exception_handler',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    
    #'DEFAULT_PAGINATION_CLASS': 'problems.pagination.InfinitePagination',
    #'PAGE_SIZE': 50,
}

# DRF Standardized Errors

DRF_STANDARDIZED_ERRORS = {
    'EXCEPTION_FORMATTER_CLASS': 'core.util.exception_handler.ExceptionFormatter',
    'EXCEPTION_HANDLER_CLASS': 'drf_standardized_errors.handler.ExceptionHandler',
}

# SimpleJWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

SIMPLE_JWT = {
    'SIGNING_KEY': SECRET_KEY,
    'ALGORITHM': 'HS256',
    'ROTATE_REFRESH_TOKENS': True,
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'BLACKLIST_AFTER_ROTATION': True,

}

# All Auth

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = '/'

# Social Account

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': env('GITHUB_CLIENT_ID'),
            'secret': env('GITHUB_CLIENT_SECRET'),
            'key': ''
        }
    },
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': ''
        }
    }
}

# Rest auth

REST_AUTH = {
    'USE_JWT': False,

    'JWT_AUTH_SECURE': True,
    'JWT_AUTH_HTTPONLY': False,
    'JWT_AUTH_SAMESITE': 'None',

    'LOGIN_SERIALIZER': 'core.user.serializers.login.UserLoginSerializer',
    'REGISTER_SERIALIZER': 'core.user.serializers.register.UserRegisterSerializer',
    'JWT_TOKEN_CLAIMS_SERIALIZER': 'core.auth.serializers.tokens.TokenObtainPairSerializer'

}

# Core.Application

COREAPP_CLIENTID_N_BYTES = 16
COREAPP_SECRET_N_BYTES = 64

# Knox

REST_KNOX = {
    'SECURE_HASH_ALGORITHM':'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64, # By default, it is set to 64 characters (this shouldn't need changing).
    'TOKEN_TTL': timedelta(minutes=45), # The default is 10 hours i.e., timedelta(hours=10)).
    'USER_SERIALIZER': 'core.user.serializers.users.UserSerializer',
    'TOKEN_LIMIT_PER_USER': None, # By default, this option is disabled and set to None -- thus no limit.
    'AUTO_REFRESH': False, # This defines if the token expiry time is extended by TOKEN_TTL each time the token is used.
}

# CORS

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://10.103.232.163:8081'
]