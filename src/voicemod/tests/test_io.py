import os
import numpy as np
from voicemod.io import read, write
from voicemod.mods import apply_mod
from voicemod.filters.volume import VolumeFilter
from voicemod.filters.pitch_shifter import PitchShiftFilter
from voicemod.filters.reverb import ReverbFilter

TEST_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = f"{TEST_FILE_PATH}/data/test.wav"
RESULT_FILE = f"{TEST_FILE_PATH}/data/result-without-changes.wav"
RESULT_FILE_VOLUME = f"{TEST_FILE_PATH}/data/result-with-volume.wav"
RESULT_FILE_PITCH = f"{TEST_FILE_PATH}/data/result-with-pitch.wav"
RESULT_FILE_REVERB = f"{TEST_FILE_PATH}/data/result-with-reverb.wav"

def test_read_write():
    frame_rate, data = read(INPUT_FILE)

    write(RESULT_FILE, data, frame_rate)

    result_frame_rate, result_data = read(RESULT_FILE)

    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, data)


def test_read_write_with_filter():
    decrease_volume = VolumeFilter(volume=0.2)

    frame_rate, data = read(INPUT_FILE)

    modified = decrease_volume.apply(frame_rate, data)
    write(RESULT_FILE_VOLUME, modified, frame_rate)

    result_frame_rate, result_data = read(RESULT_FILE_VOLUME)

    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, modified)


def test_read_write_with_pitch_shift():
    pitch_shifter = PitchShiftFilter(steps=-10)

    frame_rate, data = read(INPUT_FILE)

    modified = pitch_shifter.apply(frame_rate, data)
    write(RESULT_FILE_PITCH, modified, frame_rate)

    result_frame_rate, result_data = read(RESULT_FILE_PITCH)

    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, modified)

def test_read_write_with_reverb():
    reverb = ReverbFilter(delay=100, decay=0.5)

    frame_rate, data = read(INPUT_FILE)

    modified = reverb.apply(frame_rate, data)
    write(RESULT_FILE_REVERB, modified, frame_rate)

    result_frame_rate, result_data = read(RESULT_FILE_REVERB)

    print(modified)
    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, modified)




