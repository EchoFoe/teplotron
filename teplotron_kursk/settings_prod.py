DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': '12',
        'PASSWORD': '12',
        'HOST': 'localhost',
        'PORT': '',

    }
}
