from Django_Bigdely_Tamrin.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3ng2p$3u9c8@fh61^5v+m199c_(0i_qxk%=q10$x8e+cgtd2t0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'
COMPRESS_ENABLED = True

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

