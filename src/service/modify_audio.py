from telegram.ext import CallbackContext
from dal.audio_repository import save_audio
import voicemod.mods as voicemod

def apply_mod(audio_path: str, mod_name: str):
    voicemod.apply_mod(audio_path, mod_name)
    return audio_path