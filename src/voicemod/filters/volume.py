import numpy as np
from voicemod.filters.base import BaseFilter
import sys

MAX_INT = 2147483647

class VolumeFilter(BaseFilter):
    VOLUME_DEFAULT = 1

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        volume = self.params.get('volume', self.VOLUME_DEFAULT)

        apply_volume = np.vectorize(self.apply_volume)

        return apply_volume(data)

    def apply_volume(self, value):
        volume_factor = self.params.get('volume', self.VOLUME_DEFAULT)

        try:
            new_value = value * volume_factor
            return np.int32(new_value)
        except OverflowError:
            if value > 0:
                return np.int32(MAX_INT)
            return np.int32(-MAX_INT)