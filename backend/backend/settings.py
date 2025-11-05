"""
Django settings for backend project.

Environment-driven configuration for development and production.
"""

from pathlib import Path
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Load environment variables from .env at project root
load_dotenv(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "dev-insecure-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True").lower() in {"1", "true", "yes"}

import dj_database_url

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost,.herokuapp.com,.netlify.app').split(',')

CSRF_TRUSTED_ORIGINS = [
    "https://prairies-africa.netlify.app",
]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'corsheaders',
    # Local apps
    'customers',
    'bookings',
    'payments',
    'activities',
]

JAZZMIN_SETTINGS = {
    "site_title": "Prairies Admin",
    "site_header": "Prairies Africa",
    "site_brand": "Prairies Admin",
    "site_logo": "images/logo.png",
    "welcome_sign": "Welcome to the Prairies Africa Admin",
    "search_model": ["auth.User", "bookings.Booking"],
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Bookings", "model": "bookings.Booking"},
        {"app": "customers", "name": "Customers", "model": "customers.Customer"},
    ],
    "ui_tweaks": {
        "navbar_small_text": False,
        "footer_small_text": False,
        "body_small_text": False,
        "brand_small_text": False,
        "brand_colour": "navbar-dark",
        "accent": "accent-primary",
        "navbar": "navbar-dark",
        "no_navbar_border": False,
        "navbar_fixed": True,
        "layout_boxed": False,
        "footer_fixed": False,
        "sidebar_fixed": True,
        "sidebar": "sidebar-dark-primary",
        "sidebar_nav_small_text": False,
        "sidebar_disable_expand": False,
        "sidebar_nav_child_indent": False,
        "sidebar_nav_compact_style": False,
        "sidebar_nav_legacy_style": False,
        "sidebar_nav_flat_style": False,
        "theme": "flatly",
        "dark_mode_theme": "darkly",
        "button_classes": {
            "primary": "btn-primary",
            "secondary": "btn-secondary",
            "info": "btn-info",
            "warning": "btn-warning",
            "danger": "btn-danger",
            "success": "btn-success"
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise config for serving static files
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework defaults
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# CORS configuration
# In development, allow all origins so HTML files opened directly work
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
else:
    CORS_ALLOWED_ORIGINS = [
    'https://prairiesafrica.com',
    'https://www.prairiesafrica.com',
    'https://prairies-africa-frontend.onrender.com',
    'https://www.prairies-africa-frontend.onrender.com',
    'https://prairies-africa.netlify.app',
    'https://www.prairies-africa.netlify.app',
    'http://localhost:3000',
]
    
    FRONTEND_URL = os.getenv('FRONTEND_URL')
    if FRONTEND_URL and FRONTEND_URL not in CORS_ALLOWED_ORIGINS:
        CORS_ALLOWED_ORIGINS.append(FRONTEND_URL)

CSRF_TRUSTED_ORIGINS = [
    'https://prairiesafrica.com',
    'https://www.prairiesafrica.com',
    'https://prairies-africa.netlify.app',
]

# Email configuration (Gmail/Workspace compatible)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() in {"1", "true", "yes"}
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'no-reply@prairiesafrica.com')

# Bank Account Details
BANK_DETAILS = {
    'NAME': os.getenv('BANK_NAME', 'Standard Bank'),
    'ACCOUNT_NAME': os.getenv('BANK_ACCOUNT_NAME', 'Praires Africa'),
    'ACCOUNT_NUMBER': os.getenv('BANK_ACCOUNT_NUMBER', '123456789'),
    'BRANCH_CODE': os.getenv('BANK_BRANCH_CODE', '123456'),
    'SWIFT_CODE': os.getenv('BANK_SWIFT_CODE', 'SBZAZAJJ'),
}

# Package Pricing Information (Source of Truth)
PACKAGE_PRICES = {
    'vicfalls-chobe': {'price': 170.00, 'title': 'Victoria Falls To Chobe Group Tour'},
    'vicfalls-hwange': {'price': 285.00, 'title': 'Victoria Falls To Hwange National Park Small Group Tour'},
    'guided-lunch': {'price': 220.00, 'title': 'Victoria Falls Guided Tour With Lunch'},
    'five-day': {'price': 1200.00, 'title': '5 DAY Explore Zimbabwe, Zambia and Botswana'},
    'heli': {'price': 136.00, 'title': 'Helicopter Scenic Flight over Victoria Falls (12–13 min)'},
    'rhino-walk': {'price': 85.00, 'title': 'A Game Drive Plus White Rhino Short Walk'},
    'devils-pool': {'price': 199.00, 'title': 'Small-Group Devil\'s Pool and Livingstone Island Tour'},
    'dinner-cruise': {'price': 93.00, 'title': 'Dinner Cruise on the Zambezi River'},
    'chobe-full': {'price': 185.00, 'title': 'Full Day Tour to Chobe National Park and Botswana'},
    'chobe-small': {'price': 170.00, 'title': 'Chobe National Park Small Group Day Safari from Victoria Falls'},
}
