from telegram import File
from constants import OGG_EXTENSION

import os

AUDIOS_PATH = "tmp/audios/"

class TelegramAudioRepository():
    
    def __init__(self):
        self.create_audio_storage_dir()

    def create_audio_storage_dir(self):
        if not os.path.exists(AUDIOS_PATH):
            os.makedirs(AUDIOS_PATH)

    def save_audio(self, audio_file: File):
        file_id = update.message.voice.file_id
        file_name = PATH + file_id + OGG_EXTENSION
        audio_file.download(file_name)
        new_path = ogg_to_wav(file_name, PATH)
        return new_path