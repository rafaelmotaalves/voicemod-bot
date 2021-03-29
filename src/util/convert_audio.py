import logging

from pydub import AudioSegment
from constants import OGG_EXTENSION, WAV_EXTENSION, WAV_FORMAT

def ogg_to_wav (fileName, dest):
    logging.info("Converting " + fileName + " to wav")

    audio = AudioSegment.from_ogg(dest + fileName)

    new_path = dest + fileName.replace(OGG_EXTENSION, WAV_EXTENSION)
    audio.export(new_path, format=WAV_FORMAT, tags={"artist": "@WordBlocker"})
    
    logging.info (fileName + " converted to " + new_path)
    return new_path