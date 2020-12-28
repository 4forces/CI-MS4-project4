"""
Django settings for UpbeatEngineering project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the .env environment file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["ci-ms4-upbeatengineering.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'cloudinary',
    'mathfilters',

    # allauth apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',


    # my apps
    'products',
    'home',
    'cart',
    'checkout',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'UpbeatEngineering.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # the above line is required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents'
            ],
        },
    },
]

# / START OF ALLAUTH SETTINGS

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# user has to login with username and email
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# new users must provide an email address
ACCOUNT_EMAIL_REQUIRED = True

# sends email to users email for compulsory account verification
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# prompts user to enter email twice
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True

# username must have min 4 characters
ACCOUNT_USERNAME_MIN_LENGTH = 4

# login page url path
LOGIN_URL = '/accounts/login/'

# page displayed after login
# Changed from '/success' to '/' -> To direct to store homepage
LOGIN_REDIRECT_URL = '/'

TEST_EMAIL = os.environ.get('TEST_EMAIL')
# when working in gitpod, change 'export TEST_EMAIL = 0' at .env
if TEST_EMAIL == "1":
    # For verification email link to display in console (for debugging)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # For sending out actual emails
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")

#  END OF ALLAUTH SETTINGS /


WSGI_APPLICATION = 'UpbeatEngineering.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CLOUDINARY = {
    'cloud_name': os.environ.get("CLOUDINARY_CLOUD_NAME"),
    'api_key': os.environ.get("CLOUDINARY_API_KEY"),
    'api_secret': os.environ.get("CLOUDINARY_API_SECRET"),
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
ENDPOINT_SECRET = os.environ.get('ENDPOINT_SECRET')
