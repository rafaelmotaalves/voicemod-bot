from pydub import AudioSegment
import numpy as np


def read(filename: str) -> (int, np.array):
    audio = AudioSegment.from_file(filename)

    audio.set_channels(1)

    samples = audio.get_array_of_samples()

    return audio.frame_rate, np.array(samples)


def write(filename: str, data: np.array, frame_rate: int = 2240):
    audio = AudioSegment(
        # force 16 bit signed integer
        data=np.array(data, dtype=np.int16).tobytes(),
        channels=1,  # mono
        sample_width=2,  # 2 bytes
        frame_rate=frame_rate
    )

    audio.export(filename, format=filename.split(".")[-1])
