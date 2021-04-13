from telegram import File
from constants import OGA_EXTENSION, WAV_EXTENSION
from util.convert_audio import ogg_to_wav, wav_to_ogg

import os

AUDIOS_PATH = "tmp/audios/"

def create_audio_storage_dir():
    if not os.path.exists(AUDIOS_PATH):
        os.makedirs(AUDIOS_PATH)

def save_audio(audio_file: File):
    file_path = AUDIOS_PATH + audio_file.file_id + OGA_EXTENSION
    file_path = audio_file.download(file_path)
    file_path = ogg_to_wav(file_path)
    return file_path

def prepare_voice_response(audio_file: File):
    file_path = AUDIOS_PATH + audio_file.file_id + WAV_EXTENSION
    file_path = wav_to_ogg(file_path)
    return file_path

create_audio_storage_dir()