from telegram.ext import CallbackContext 
from telegram import Update

VOICE_MODS = ["teste", "oi", "abc"]

class ListModsCommand():
    command  = "list_mods"

    def callback(self, update: Update, context: CallbackContext):
        update.message.reply_text(f"The voicemod options are: {', '.join(VOICE_MODS)}")