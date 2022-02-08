import os
from .base_settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1", "localhost", 'http://content-bulk.online', 'https://content-bulk.online']
CORS_ALLOWED_ORIGINS = ['http://content-bulk.online', 'https://content-bulk.online']
CSRF_TRUSTED_ORIGINS = ['http://content-bulk.online', 'https://content-bulk.online']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
STATIC_ROOT = os.environ.get('STATIC_ROOT')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '{levelname} | {asctime} | {module} - {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'rest_api_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/rest_api.log',
            'when': 'D',
            'interval': 1,
            'level': 'INFO',
            'formatter': 'file'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['rest_api_file'],
            'level': 'INFO',
        },
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://a96a45cf6450472993682f1c2d76117a@o1136667.ingest.sentry.io/6188810",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)
