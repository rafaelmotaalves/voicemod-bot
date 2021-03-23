from env import get_env, EnvVar
from telegram.ext import Updater

from log import config_logger 
from commands import register_commands

TELEGRAM_TOKEN = get_env(EnvVar.telegram_token)

def main():
    config_logger()
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    register_commands(dispatcher)

    updater.start_polling()

if __name__ == "__main__":
    main()