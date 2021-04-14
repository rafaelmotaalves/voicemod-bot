from telegram.ext import CallbackContext 
from telegram import Update
from dal.audio_repository import save_audio, prepare_voice_response

MOD_NAME_KEY = "mod_name"

def download_audio(update: Update, context: CallbackContext):
    file_id = update.message.voice.file_id
    audio_file = context.bot.get_file(file_id)
    return save_audio(audio_file)

def prepare_voice_note(update: Update, context: CallbackContext):
    file_id = update.message.voice.file_id
    audio_file = context.bot.get_file(file_id)
    return prepare_voice_response(audio_file)

def get_user_mod_name(context: CallbackContext):
    return context.user_data.get(MOD_NAME_KEY)

def set_user_mod_name(context: CallbackContext, value: str):
    context.user_data[MOD_NAME_KEY] = value