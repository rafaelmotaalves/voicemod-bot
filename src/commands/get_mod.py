from telegram.ext import CallbackContext 
from telegram import Update

from commands.constants import MOD_NAME

class GetModCommand():
    command  = "get_mod"

    def callback(self, update: Update, context: CallbackContext):
        if MOD_NAME in context.user_data:
            mod_name = context.user_data.get(MOD_NAME)

            update.message.reply_text(f"Your current voicemod is: {mod_name}")
        else:
            update.message.reply_text(f"Your currently have no voicemods enabled")