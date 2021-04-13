from telegram.ext import CallbackContext 
from telegram import Update, Bot
from voicemod.mods import list_mods


class ListModsCommand():
    command  = "list_mods"

    def callback(self, update: Update, context: CallbackContext):
        update.message.reply_text(f"The voicemod options are: {', '.join(list_mods())}")
