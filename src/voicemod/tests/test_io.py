import os
import numpy as np
from voicemod.io import read, write
from voicemod.filters.volume import VolumeFilter


TEST_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
RESULT_FILE = f"{TEST_FILE_PATH}/data/result.wav"
WITH_FILTER_RESULT_FILE = f"{TEST_FILE_PATH}/data/result-with-filter.wav"
INPUT_FILE = f"{TEST_FILE_PATH}/data/test.wav"

def test_read_write():
    frame_rate, data = read(INPUT_FILE)

    write(RESULT_FILE, data, frame_rate)

    result_frame_rate, result_data = read(RESULT_FILE)

    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, data)

def test_read_write_with_filter():
    decrease_volume = VolumeFilter(volume=0.2)

    frame_rate, data = read(INPUT_FILE)

    modified = decrease_volume.apply(data)
    write(WITH_FILTER_RESULT_FILE, modified, frame_rate)

    result_frame_rate, result_data = read(WITH_FILTER_RESULT_FILE)

    assert frame_rate == result_frame_rate
    assert np.array_equal(result_data, modified)

def teardown_function():
    for test_file in [RESULT_FILE, WITH_FILTER_RESULT_FILE]:
        if os.path.exists(test_file):
            os.remove(test_file)

