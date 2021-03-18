from .base import *

ALLOWED_HOSTS = ['*'] #dışarıdan herkesin istek yapabilmesi

DEBUG = config('DEBUG', default=True, cast=bool)


#developmentte şifreyi valide etme


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

