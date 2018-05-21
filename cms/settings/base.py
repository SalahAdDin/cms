import os
from django.utils.translation import ugettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random

            SECRET_KEY = ''.join(
                [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]
            )
            secret = open(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

SITE_TITLE = 'Rotafilo'
SITE_HEADER = _('Rotafilo Savunma Havacılık ve Enerji Teknolojileri San. ve Tic. Ltd. Şti.')

# Application definition

PROJECT_APPS = [
    'about',
    # 'blog',
    'core',
    # 'home',
    # 'person',
    # 'products',
    'search',
]

THIRD_PARTY_APPS = [
    'wagtail.api.v2',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.sitemaps',
    "wagtail.contrib.table_block",
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'axes',
    # 'django_celery_beat',
    # 'django_celery_results',
    'django_extensions',
    # 'disqus',
    'embed_video',
    'modelcluster',
    'robots',
    'taggit',
    'condensedinlinepanel',
    # 'wagtailcodeblock',
    'wagtailblocks_cards',
    'wagtail_embed_videos',
    'wagtail_feeds',
    'wagtailgeowidget',
    'wagtailmenus',
    'wagtailmetadata',
    'wagtailstreamforms',
    # 'wagtailtranslations',
    'webpack_loader',
]

INSTALLED_APPS = PROJECT_APPS + THIRD_PARTY_APPS + [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',

    'wagtail.contrib.settings',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',

    # silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'cms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',

                'wagtail.contrib.settings.context_processors.settings',
                'wagtailmenus.context_processors.wagtailmenus',

                'core.context_processors.analytics',
                'core.context_processors.utils',
            ],
        },
    },
]

WSGI_APPLICATION = 'cms.wsgi.application'

# Authentication backends
# # https://docs.djangoproject.com/en/2.0/ref/settings/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesModelBackend',
    'django.contrib.auth.backends.ModelBackend'
]

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGES = WAGTAILADMIN_PERMITTED_LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
    ('tr', _('Turkish')),
]

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Wagtail settings

WAGTAIL_SITE_NAME = SITE_TITLE

WAGTAIL_AUTO_UPDATE_PREVIEW = True
WAGTAILADMIN_RECENT_EDITS_LIMIT = 10
WAGTAIL_ENABLE_UPDATE_CHECK = True
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAILADMIN_NOTIFICATION_USE_HTML = True

WAGTAILIMAGES_IMAGE_MODEL = 'core.CMSImage'
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 5 * 1024 * 1024

WAGTAILSITEMAPS_CACHE_TIMEOUT = 60 * 60 * 24

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': [
                'bold',
                'italic',
                'underline',
                'strikethrough',
                'mark',
                'quotation',
                'keyboard',
                'h2',
                'h3',
                'h4',
                'ol',
                'ul',
                'hr',
                'embed',
                'link',
                'document-link',
                'image',
                'blockquote'
            ],
        }
    },
}

# Google maps
GEO_WIDGET_DEFAULT_LOCATION = {
    'lat': 39.776667,
    'lng': 30.520556
}

# Axes
AXES_COOLOFF_TIME = 24
AXES_LOGIN_FAILURE_LIMIT = 3
AXES_LOCKOUT_TEMPLATE = '429.html'
AXES_USE_USER_AGENT = True

# Robots
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24
ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

# Embed videos
EMBED_VIDEO_BACKENDS = [
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
    'embed_video.backends.SoundCloudBackend',
]

EMBED_VIDEO_TIMEOUT = 10

# Celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Webpack
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'STATS_FILE': os.path.join(PROJECT_DIR, 'static', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    },
    'JQUERY': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(PROJECT_DIR, 'static', 'jquery-webpack-stats.json'),
    }
}
