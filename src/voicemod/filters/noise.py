import numpy as np
from voicemod.filters.base import BaseFilter

class NoiseFilter(BaseFilter):
    DEFAULT_DENSITY = 1

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        density = self.params.get("density", self.DEFAULT_DENSITY)

        sigma = density * np.sqrt(frame_rate/2)
        noise = np.random.normal(0,sigma,data.size)
        return data+noise