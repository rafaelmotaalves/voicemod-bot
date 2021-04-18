from pydub import AudioSegment
import numpy as np

MAX_INT = 2147483647

def safe_cast_to_int32(value):
    try:
        return np.int32(value)
    except OverflowError:
        return np.int32(MAX_INT if value > 0 else -MAX_INT)

def create_segment(data: np.array, frame_rate: int) -> AudioSegment:
    return AudioSegment(
        data=np.array(data, dtype=np.int32).tobytes(),
        channels=1,  # mono
        sample_width=4,  # bytes
        frame_rate=frame_rate
    )