from telegram.ext import CallbackContext 
from telegram import Update
from dal.audio_repository import save_audio
from service.modify_audio import apply_mod
from util.telegram import get_user_mod_name, download_audio

MESSAGE_PREFIX = "Audio from @"
FILE_OPEN_MODE = "rb"

class ModifyAudioHandler():
    def callback(self, update: Update, context: CallbackContext):
        mod_name = get_user_mod_name(context)
        if mod_name:
            audio_path = download_audio(update, context)
            apply_mod(audio_path, mod_name)
            update.message.reply_audio(open(audio_path, FILE_OPEN_MODE), title=MESSAGE_PREFIX + update.message.from_user.username)
            update.message.delete()
