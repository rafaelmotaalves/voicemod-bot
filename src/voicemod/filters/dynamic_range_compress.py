from voicemod.filters.base import BaseFilter
from voicemod.util import create_segment
from pydub import effects
import numpy as np

class DynamicRangeCompress(BaseFilter):
    DEFAULT_THRESHOLD = -20
    DEFAULT_RATIO = 4
    DEFAULT_ATTACK = 5
    DEFAULT_RELEASE = 50

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        # The threshold in -dBFS, begin 0 the max value
        threshold = self.params.get("threshold", self.DEFAULT_THRESHOLD)
        # the ratio in which will reduce audio below the wanted the threshold
        ratio = self.params.get("ratio", self.DEFAULT_RATIO)
        # how long it takes to start compression once the value exceeded the threshold
        attack = self.params.get("attack", self.DEFAULT_ATTACK)
        # how long it takes to stop compression once the value falled before the threshold
        release = self.params.get("release", self.DEFAULT_RELEASE)

        segment = create_segment(data, frame_rate)

        result = effects.compress_dynamic_range(
            segment, 
            threshold=threshold, 
            ratio=ratio, 
            attack=attack, 
            release=release
        )

        return result.get_array_of_samples()