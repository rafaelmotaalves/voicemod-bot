from librosa.effects import time_stretch
import numpy as np

from voicemod.filters.base import BaseFilter

class WhaleFilter(BaseFilter):
    DEFAULT_RATE = 0.3

    def execute(self, frame_rate: int, data: np.array) -> np.array:

        rate = self.params.get('rate', self.DEFAULT_RATE)

        return time_stretch(data.astype(np.float), rate).astype(np.int32)
