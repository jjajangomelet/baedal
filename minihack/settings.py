"""
Django settings for minihack project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ij8)s#)^w0awkleime39!dsw555$4hp^-0ve(z7&%*49v^)%^r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'orders.apps.OrdersConfig',

    #allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.kakao',

    #social-auth-app
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
    # 기본 인증 백엔드
    'allauth.account.auth_backends.AuthenticationBackend', # 추가 
]

# 디폴트 SITE의 ID
# 등록하지 않으면 각 요청 시에 host명의 site 인스턴스를 찾음
SITE_ID = 1

LOGIN_REDIRECT_URL = 'accounts:login' # 로그인 후 리디렉션 할 페이지 
ACCOUNT_LOGOUT_REDIRECT_URL = 'accounts:login' # 로그아웃 후 리디렉션 할 페이지
ACCOUNT_LOGOUT_ON_GET = True # 로그아웃 버튼 클릭 시 자동 로그아웃
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 로그인 인증 방법
ACCOUNT_EMAIL_REQUIRED = True # 이메일 로그인 인증시 반드시 따라와야됨.
SOCIALACCOUNT_AUTO_SIGNUP = False # SNS 인증 바로 가입 X
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.SignupForm'
AUTH_USER_MODEL = 'accounts.Accounts'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'minihack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'minihack', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug' : DEBUG,
        },
    },
]

WSGI_APPLICATION = 'minihack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'accounts', 'static'),
    os.path.join(BASE_DIR, 'orders', 'static'),
    os.path.join(BASE_DIR, 'minihack', 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

