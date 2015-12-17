# For production, change this to import from settings.production
from settings.base import *

#Add proper database name, user and password here, if necessary
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'apex.ttu.ee',
        'NAME': 'apex',
        'USER': 't135192',
        'PASSWORD': '1kolekoll',
        'PORT': '7301'
    }
}

# For production, override SECRET_KEY


# # For development:
# # Debug toolbar
# INSTALLED_APPS.append('debug_toolbar')
# INTERNAL_IPS = ('127.0.0.1',)
#
# # Show emails in console, don't send them
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
