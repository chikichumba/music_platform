from .base import *

SERVICE_NAME = 'users'

INSTALLED_APPS = INSTALLED_APPS + [
    'apps.users',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'music_platform',
        'USER': 'music_pahan',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',        
        'ATOMIC_REQUESTS': True,
    }
}

ROOT_URLCONF = 'apps.users.urls'
