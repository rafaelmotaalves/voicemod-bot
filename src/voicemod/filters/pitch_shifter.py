from librosa.effects import pitch_shift
import numpy as np

from voicemod.filters.base import BaseFilter

class PitchShiftFilter(BaseFilter):
    DEFAULT_STEPS = 0

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        steps = self.params.get('steps', self.DEFAULT_STEPS)

        return pitch_shift(data.astype(np.float), frame_rate, steps).astype(np.int32)
