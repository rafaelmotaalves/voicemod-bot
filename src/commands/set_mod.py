from telegram.ext import CallbackContext 
from telegram import Update, Bot
from util.telegram import set_user_mod_name

class SetModCommand():
    command  = "set_mod"

    def callback(self, update: Update, context: CallbackContext):
        if len(context.args) > 0:
            mod_name = context.args[0]
            set_user_mod_name(context, mod_name)
            update.message.reply_text(f"Your voicemod was set: {mod_name}")
        else:
            update.message.reply_text(f"Invalid voicemod name")
