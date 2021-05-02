from telegram.ext import CallbackContext 
from telegram import Update
from voicemod.mods import list_mods


class ListModsCommand():
    command  = "list_mods"

    def callback(self, update: Update, context: CallbackContext):
        mods = map(lambda x: " - " + x, list_mods())

        update.message.reply_text("The voicemod options are:\n" + "\n".join(mods))
