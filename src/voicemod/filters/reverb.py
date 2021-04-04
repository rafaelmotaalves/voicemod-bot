import numpy as np
from voicemod.filters.base import BaseFilter
from voicemod.util import safe_cast_to_int32

class ReverbFilter(BaseFilter):
    DELAY_DEFAULT = 100
    DECAY_DEFAULT = 0.5

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        delay = self.params.get('delay', self.DELAY_DEFAULT)
        decay = self.params.get('decay', self.DECAY_DEFAULT)

        delay_in_samples = self.get_delay_in_samples(frame_rate, delay)
        result = np.array(data)

        for i in range(len(result) - delay_in_samples):
            new_value = result[i + delay_in_samples] + result[i] * decay

            result[i + delay_in_samples] = safe_cast_to_int32(new_value)

        return result

    def get_delay_in_samples(self,frame_rate, delay):
        frames_per_millisecond = int(frame_rate / 1000.0)

        return delay * frames_per_millisecond
