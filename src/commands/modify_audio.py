from telegram.ext import CallbackContext 
from telegram import Update, InputFile
from dal.audio_repository import save_audio
from service.modify_audio import apply_mod
from util.telegram import get_user_mod_name, download_audio, prepare_voice_note
from constants import OGG_EXTENSION


MESSAGE_PREFIX = "Audio from @"
FILE_OPEN_MODE = "rb"

class ModifyAudioHandler():
    def callback(self, update: Update, context: CallbackContext):
        mod_name = get_user_mod_name(context)
        if mod_name:
            audio_path = download_audio(update, context)
            apply_mod(audio_path, mod_name)
            bot = context.bot
            modded_audio_path = prepare_voice_note(update, context)
            
            audio_data = open(modded_audio_path, FILE_OPEN_MODE)
            voice = InputFile(obj=audio_data.read(), filename=MESSAGE_PREFIX+update.message.from_user.username+OGG_EXTENSION)
            bot.sendVoice(chat_id=update.message.chat_id, voice=voice, caption=MESSAGE_PREFIX+update.message.from_user.username, reply_to_message_id=update.message.message_id)
            #update.message.reply_audio(open(audio_path, FILE_OPEN_MODE), title=MESSAGE_PREFIX + update.message.from_user.username)
            audio_data.close()
            update.message.delete()
            print('RECEIVED AUDIO PATH:' + modded_audio_path)

