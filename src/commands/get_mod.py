from telegram.ext import CallbackContext 
from telegram import Update

class GetModCommand():
    command  = "get_mod"

    def callback(self, update: Update, context: CallbackContext):
        mod_name = get_user_mod_name(context)
        
        if mod_name:
            update.message.reply_text(f"Your current voicemod is: {mod_name}")
        else:
            update.message.reply_text(f"Your currently have no voicemods enabled")