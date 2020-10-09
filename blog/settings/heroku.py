# O pacote django-environ foi instalado para poder utilizar o módulo environ.
from environ import Env
from blog.settings.base import *

env = Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {'default': env.db(), }
