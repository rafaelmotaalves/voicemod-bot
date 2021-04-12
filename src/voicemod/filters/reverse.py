import numpy as np
from voicemod.filters.base import BaseFilter
import sys

class ReverseFilter(BaseFilter):
    def execute(self, frame_rate: int, data: np.array) -> np.array:
        data = np.flip(data)
        reverse_data = np.vectorize(self.reverse_data)
        return reverse_data(data)

    def reverse_data(self, value):
        reversed_data = np.flip(value)
        return reversed_data
