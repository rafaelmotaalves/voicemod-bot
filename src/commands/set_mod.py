from telegram.ext import CallbackContext 
from telegram import Update

from commands.constants import MOD_NAME

class SetModCommand():
    command  = "set_mod"

    def callback(self, update: Update, context: CallbackContext):
        if len(context.args) > 0:
            mod_name = context.args[0]

            context.user_data[MOD_NAME] = mod_name

            update.message.reply_text(f"Your voicemod was set: {mod_name}")
        else:
            update.message.reply_text(f"Invalid voicemod name")