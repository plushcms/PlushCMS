#-*- coding: utf-8 -*-

PLUSH_VERSION = "0.1.1"
UPDATE_DATE = "29.04.11"

# Configure contact form 
SERVER = ""
PORT = 0
LOGIN = ""
PASSWORD = ""
SENDER = ""
RECIPIENT = ""

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

TIME_ZONE = ""
LANGUAGE_CODE = ""

SITE_ID = 1

USE_I18N = True
USE_L10N = True

# JavaScript, CSS nad image reference path ("/img" is static)
MEDIA_ROOT = "/img"
# Upload photos directory ("/img/photoGallery" is static)
MEDIA_GALLERY = "/img/photoGallery"
# Upload files directory ("/img/uploadFiles" is static)
MEDIA_STORAGE = "/img/uploadFiles"
# Font file path used by captcha image generator ("/img/fonts/captcha.ttf" is static)
MEDIA_FONT = "/img/fonts/captcha.ttf"
# URL used for managing stored files ("/img/" is static)
MEDIA_URL = "/img/"

# Templates path ("/core/templates/" is static)
TEMPLATE_DIRS = (
    "/core/templates/",
)

ADMIN_MEDIA_PREFIX = "/media/"

SECRET_KEY = "k$-y&py2a&^or_)_eps52jv^-^yh^^gq0u_2-)q#xvar7ia&+5"

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "plushcms.processors.showCategories",
    "plushcms.processors.showLinks",
    "plushcms.processors.showTopNews",
    "plushcms.processors.showPartners",
    "plushcms.processors.showSearchForm",
    "plushcms.processors.showSystemDetails",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.csrf.CsrfResponseMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

ROOT_URLCONF = "plushcms.urls"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "plushcms.core",
    "plushcms.gallery",
    "plushcms.storage",
    "plushcms.treemenus",
)
