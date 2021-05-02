from telegram.ext import CallbackContext 
from telegram import Update
from util.telegram import set_user_mod_name
from voicemod.mods import list_mods


class SetModCommand():
    command  = "set_mod"

    def callback(self, update: Update, context: CallbackContext):
        if len(context.args) > 0 and not update.edited_message:
            mod_name = context.args[0]
            if mod_name in list_mods():
                set_user_mod_name(context, mod_name)
                update.message.reply_text(f"Your voicemod was set: {mod_name}")
                return
        update.message.reply_text(f"Invalid voicemod name")
