import os
from dotenv import load_dotenv

from .base import *  # noqa

SECRET_KEY = os.getenv("SECRET_KEY")


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", ["*"])

load_dotenv()


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": 5432,
    }
}
