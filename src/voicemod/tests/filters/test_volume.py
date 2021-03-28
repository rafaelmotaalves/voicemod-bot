from voicemod.filters.volume import VolumeFilter
from voicemod.filters.base import BaseFilter
import numpy as np

def test_mute():
    filter = VolumeFilter(volume=0)

    result = filter.apply(np.array([1, 2, 3, 4]))

    assert np.all(result==0)

def test_volume_down():
    filter = VolumeFilter(volume=0.5)

    result = filter.apply(np.array([2, 2, 2, 2]))

    assert np.all(result==1)

def test_volume_up():
    filter = VolumeFilter(volume=2)

    result = filter.apply(np.array([1, 1, 1, 1]))

    assert np.all(result==2)
