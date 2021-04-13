import logging

from pydub import AudioSegment
from constants import OGA_EXTENSION, WAV_EXTENSION, WAV_FORMAT, OGG_EXTENSION
import subprocess

ARTIST = "@VoiceModBot"

def ogg_to_wav (file_path: str):
    logging.info("Converting " + file_path + " to wav")

    audio = AudioSegment.from_ogg(file_path)

    new_path = file_path.replace(OGA_EXTENSION, WAV_EXTENSION)
    audio.export(new_path, format=WAV_FORMAT, tags={"artist": ARTIST})
    
    logging.info (file_path + " converted to " + new_path)
    return new_path

def wav_to_ogg (file_path: str):
    logging.info("Converting " + file_path + " to ogg")

    audio = AudioSegment.from_ogg(file_path)
    new_path = file_path.replace(WAV_EXTENSION, OGG_EXTENSION)
    subprocess.run(["ffmpeg", '-i', file_path, '-acodec', 'libopus', new_path, '-y'])
    
    logging.info (file_path + " converted to " + new_path)
    return new_path