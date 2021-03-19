import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .base import *

#production ortamında başlatmak için:python manage.py  runserver --settings=config.settings.production



ALLOWED_HOSTS = ['ugurhmz.com','127.0.0.1','3.23.98.144'] #dışarıdan sadece bu istek yapabilmesi
DEBUG = config('DEBUG', default=False, cast=bool)
#production ortamında şifreyi valid et
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#production da farklı db çalıştır
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}


sentry_sdk.init(
    dsn=config('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)


AWS_ACCESS_KEY_ID=config('ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=config('SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME='ugurhmzs3'
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400',
}
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)
STATICFILES_STORAGE ='storages.backends.s3boto3.S3Boto3Storage'

#yukardakinden sonra şunu consolda yap:
# python manage.py collectstatic --settings=config.settings.development


DEFAULT_FILE_STORAGE='config.storage_backend.MediaStorage' #bütün dosyalar başarılı şekilde
