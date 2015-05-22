# -*- coding: utf-8 -*-
"""
Django settings for {{ project_name }} project.
"""
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '{{ secret_key }}')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',

	# Dependecies.
	'django_extensions',

	# Apps.
	#'{{ project_name }}.apps.<app_name>',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'debug': os.environ.get('DEBUG', True),
			'loaders': (
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
			),
			'string_if_invalid': 'Invalid variable!',
		},
	},
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'yourdatabasename.db'),
	}
	# 'default': {
	# 	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	# 	'NAME': os.environ.get('DATABASE_NAME', '{{ project_name }}'),
	# 	'USER': os.environ.get('DATABASE_USER', '{{ project_name }}'),
	# 	'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'password'),
	# 	'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
	# 	'PORT': os.environ.get('DATABASE_PORT', '5432'),
	# }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'Info <info@email.com>'
SERVER_EMAIL = 'Alerts <alerts@email.com>'

ADMINS = (
	('Admin', 'admin@email.com'),
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'default': {
			'format': '%(asctime)s  [%(name)s:%(lineno)s]  %(levelname)s - %(message)s',
		},
		'simple': {
			'format': '%(levelname)s %(message)s',
		},
	},
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		}
	},
	'handlers': {
		'null': {
			'level': 'DEBUG',
			'class': 'logging.NullHandler',
		},
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'default',
		},
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler',
		}
	},
	'loggers': {
		'django.security.DisallowedHost': {
			'handlers': ['null'],
			'propagate': False,
		},
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		'': {
			'handlers': ['console', ],
			'level': 'INFO',
		}
	}
}
