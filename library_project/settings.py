
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Installed Apps
INSTALLED_APPS = [
     'jazzmin',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'library_app',
]


# Middleware
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
]


# URL Configuration
ROOT_URLCONF = 'library_project.urls'


# Templates
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


# WSGI
WSGI_APPLICATION = 'library_project.wsgi.application'


# Database
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Language
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static Files
STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {

    "site_title": "Library Admin",

    "site_header": "Library Management",

    "site_brand": "Smart Library",

    "welcome_sign": "Welcome to Smart Library Dashboard",

    "copyright": "Library Management System",

    "search_model": ["auth.User"],

    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],

    "show_sidebar": True,

    "navigation_expanded": True,

    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",

        "library_app.Book": "fas fa-book",

        "library_app.Student": "fas fa-user-graduate",
    },

    "theme": "darkly",
}


MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

