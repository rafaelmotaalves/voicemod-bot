import os
from enum import Enum

class EnvVar(Enum):
    telegram_token = "TELEGRAM_TOKEN"

def get_env(enviroment_var):
    return os.environ.get(enviroment_var.value)