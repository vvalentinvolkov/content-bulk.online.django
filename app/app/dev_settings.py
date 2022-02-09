from .base_settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secret_key')
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://localhost:3001', 'http://127.0.0.1:3000', 'http://127.0.0.1:3001']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite3',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '{levelname} | {asctime} | {module} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'test_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/test.log',
            'level': 'DEBUG',
            'formatter': 'file'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['test_file'],
            'level': 'INFO',
        },
        'zen': {
            'handlers': ['test_file'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}