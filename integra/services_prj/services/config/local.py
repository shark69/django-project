from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbintegra',
        'USER': 'integrauser',
        'PASSWORD': 'integrapwd',
        'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}