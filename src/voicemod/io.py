import logging
from pydub import AudioSegment
import numpy as np
from voicemod.util import create_segment

def read(filename: str) -> (int, np.array):
    audio = AudioSegment.from_file(filename)

    audio.set_channels(1)

    samples = audio.get_array_of_samples()

    return audio.frame_rate, np.array(samples)


def write(filename: str, data: np.array, frame_rate: int = 44100):
    audio = create_segment(data, frame_rate)
    audio.export(filename, format=filename.split(".")[-1])
