import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()


ENV_SETTING = "ENVIRONMENT"


current_env = os.getenv(ENV_SETTING)


if current_env == "PRODUCTION":
    from settings.production import *  # noqa
elif current_env == "STAGING":
    from settings.staging import *  # noqa
elif current_env == "DEVELOPMENT":
    from settings.local import *  # noqa
else:
    raise ImproperlyConfigured("Set {} environment variable.".format(ENV_SETTING))
