from settings import *
import os

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# DBHOST is only the server name, not the full URL
hostname = os.environ['DBHOST']

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
        'NAME': "terrariopedia_website",
        'HOST': "mysql-terrariopedia.alwaysdata.net",
        'USER': "305219",
        'PASSWORD': "Nebularis2018!"
    }
}