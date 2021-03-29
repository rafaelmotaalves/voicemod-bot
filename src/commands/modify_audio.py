from telegram.ext import CallbackContext 
from telegram import Update
from commands.constants import MOD_NAME
from util.convert_audio import ogg_to_wav
from voicemod.mods import apply_mod
from dal.audio_repository import TelegramAudioRepository

class ModifyAudioHandler():
    MESSAGE_PREFIX = "Audio from @"
    FILE_OPEN_MODE = "RB"

    def __init__(self, audio_repository: TelegramAudioRepository):
        self.audio_repository = audio_repository

    def callback(self, update: Update, context: CallbackContext):
        if self.is_modifiable_audio(context):
            audio_path = self.download_audio(update, context)
            mod_name = context.user_data.get(MOD_NAME)
            apply_mod(audio_path, mod_name)
            update.message.reply_audio(open(audio_path, FILE_OPEN_MODE), title=MESSAGE_PREFIX + update.message.from_user.username)
            update.message.delete()
    
    def is_modifiable_audio(self, context: CallbackContext):
        return len(context.args) > 0 and MOD_NAME in context.user_data
    
    def download_audio(self, update: Update, context: CallbackContext):
        file_id = update.message.voice.file_id
        audio_file = context.bot.get_file(file_id)
        return self.audio_repository.save_audio(audio_file)