# Django settings for intercambios project.
import os
import json
from django.contrib.messages import constants as messages


#cambiar el nombre de messages.info a que sea message.information
#de esta forma los mensajes son compatibles con el API que trae por default noty.js
# 20 : es el numero de peso que tiene ese mensaje (importancia)
MESSAGE_TAGS = {
    messages.INFO: '',
    20: 'information',
}



#Se especifica el nombre del modelo custom de usuario
AUTH_USER_MODEL = 'intercambios.Usuario'
PROJECT_PATH = os.path.dirname(__file__)

LOGIN_URL = '/login/'




ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = (
    '127.0.0.1',
                )

#se carga config.json de prueba
os.chdir(os.path.dirname(__file__))
SETTINGS = json.loads(open('../config.json').read())

#se cargan la configuracion de la base de datos del config.json externo al proyecto
#solo si no es desde heroku
if not (os.environ.get('DATABASE_URL')):      
    SETTINGS = json.loads(open('../../config.json').read())

DATABASES = {
    'default': {
        'ENGINE': SETTINGS['DEFAULT_DATABASE_ENGINE'], 
        'NAME': SETTINGS['DEFAULT_DATABASE_NAME'],                   
        'USER': SETTINGS['DEFAULT_DATABASE_USER'],
        'PASSWORD': SETTINGS['DEFAULT_DATABASE_PASS'],
        'HOST': SETTINGS['DEFAULT_DATABASE_HOST'],            
        'PORT': SETTINGS['DEFAULT_DATABASE_PORT'],
    }
}

DEBUG = SETTINGS['DEBUG']
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*','http://intercambios.herokuapp.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chihuahua'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-MX'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '00@k_)-*$7%(c1584!m%7vuc)$)+x%y6lz6qv@&45mz%3$@y07'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_type_backends',
                               )
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'intercambios.custom_middleware.NombreMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'intercambios.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'intercambios.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = [
    'django.contrib.humanize',
    'django_admin_bootstrapped',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
#     'django.contrib.admindocs',
    'django_extensions',
    'intercambios',
    'south',
    'social_auth'
    
]

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',
)
if not (os.environ.get('DATABASE_URL')): 
    GOOGLE_OAUTH2_CLIENT_ID      = SETTINGS['GOOGLE_OAUTH2_CLIENT_ID']
    GOOGLE_OAUTH2_CLIENT_SECRET  = SETTINGS['GOOGLE_OAUTH2_CLIENT_SECRET']
    
    FACEBOOK_APP_ID = SETTINGS['FACEBOOK_APP_ID']
    FACEBOOK_API_SECRET = SETTINGS['FACEBOOK_API_SECRET']
    
else:
    
    GOOGLE_OAUTH2_CLIENT_ID      = os.environ.get('GOOGLE_ID')
    GOOGLE_OAUTH2_CLIENT_SECRET  = os.environ.get('GOOGLE_SECRET')
    
    FACEBOOK_APP_ID = os.environ.get('FACEBOOK_ID')
    FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_SECRET')
    
FACEBOOK_EXTENDED_PERMISSIONS = ['email']

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/'

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/perfil/usuario/'

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL

SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 40


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

## Heroku necessary configuration ####

if(os.environ.get('DATABASE_URL')):

    INSTALLED_APPS.append('gunicorn')
    
# Parse database configuration from $DATABASE_URL

    import dj_database_url

    DATABASES['default'] =  dj_database_url.config()

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']

    # Static asset configuration
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    
    try:
        EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
        EMAIL_HOST= 'smtp.sendgrid.net'
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True
        EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    except:
        pass
    
    



