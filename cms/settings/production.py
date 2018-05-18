from .base import *

DEBUG = False

ALLOWED_HOSTS = ['..com', '..com.']

ADMINS = [
    ('José Luis Sandoval Alaguna', 'alagunasalahaddin@live.com'),
]

# Application definition
INSTALLED_APPS += [
    'silk',
    'storages',
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
        'CONN_MAX_AGE': 1000,
        'ATOMIC_REQUESTS': True,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

# File storage
# https://docs.djangoproject.com/en/2.0/ref/files/storage/
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Cache
# https://docs.djangoproject.com/en/2.0/topics/cache/
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        'KEY_PREFIX': 'cms',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    }
}
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
MEDIA_ROOT = ''
STATIC_ROOT = ''

# Session
# https://docs.djangoproject.com/en/2.0/topics/http/sessions/#using-cached-sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Email
# https://docs.djangoproject.com/en/2.0/topics/email/
EMAIL_BACKEND = ''
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[]'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'oficial@.com'
SERVER_EMAIL = 'oficial@.com'

# AWS
AWS_HEADERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_ACCESS_KEY_ID = ''
AWS_S3_HOST = ''
AWS_S3_SECRET_ACCESS_KEY = ''
AWS_S3_SECURE_URLS = True
AWS_STORAGE_BUCKET_NAME = ''

# Analytics
GOOGLE_ANALYTICS_CODE = ''

# Google maps
GOOGLE_MAPS_V3_APIKEY = ''
GOOGLE_MAPS_V3_LANGUAGE = 'tr'
GEO_WIDGET_ZOOM = 8

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'

# Robots
ROBOTS_SITEMAP_URLS = [
    'https://.com/sitemap.xml',
]

# Secure
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True

# Silk
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
SILKY_MAX_REQUEST_BODY_SIZE = -1  # Silk takes anything <0 as no limit
SILKY_MAX_RESPONSE_BODY_SIZE = 1024  # If response body>1024kb, ignore
SILKY_META = True
SILKY_MAX_RECORDED_REQUESTS = 10 ** 4

SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
SILKY_PYTHON_PROFILER_RESULT_PATH = os.path.join(PROJECT_DIR, 'silky_profiles')

# Wagtail
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'notification@'
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True

# Celery
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_SEND_TASK_ERROR_EMAILS = True

# Webpack
WEBPACK_LOADER['DEFAULT']['CACHE'] = True
WEBPACK_LOADER.update({
    'BUNDLE_DIR_NAME': 'dist/',
    'STATS_FILE': os.path.join(PROJECT_DIR, 'static', 'webpack-stats-prod.json')
})

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'logstash': {
            '()': 'logstash_async.formatter.DjangoLogstashFormatter',
            'message_type': 'python-logstash',
            'fqdn': False,
            'extra_prefix': 'prod',
            'extra': {
                'application': PROJECT_DIR,
                'project_path': BASE_DIR,
                'environment': 'production'
            },
            'tags': ['core', 'django.request', 'django.security', 'wagtail'],
        },
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'config/logs/%s.log' % SITE_TITLE.lower()),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 50,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'error.log'
        },
        'logstash': {
            'level': 'ERROR',
            'class': 'logstash_async.handler.AsynchronousLogstashHandler',
            'transport': 'logstash_async.transport.TcpTransport',
            'host': 'logstash.host.tld',
            'port': 5959,
            'database_path': '{}/logstash.db'.format(PROJECT_DIR),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'logstash'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['logstash', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            'formatter': 'verbose',
        },
        'core': {
            'handlers': ['file', 'logstash', 'mail_admins'],
            'propagate': True,
            'level': 'ERROR',
            'formatter': 'verbose',
        },
        'wagtail': {
            'handlers': ['file', 'logstash', 'mail_admins'],
            'level': 'INFO',
            'propagate': False,
            'formatter': 'verbose',
        },
        'django.security': {
            'handlers': ['logstash', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'verbose',
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
