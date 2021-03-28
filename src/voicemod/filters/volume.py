import numpy as np
from voicemod.filters.base import BaseFilter

class VolumeFilter(BaseFilter):
    VOLUME_DEFAULT = 1

    def execute(self, data: np.array) -> np.array:
        volume = self.params.get('volume', self.VOLUME_DEFAULT)

        apply_volume = np.vectorize(lambda x: np.int16(x * volume))

        return apply_volume(data)
