import numpy as np


class BaseFilter:
    def __init__(self, inner_filter=None, **kwargs):
        self.inner_filter = inner_filter
        self.params = kwargs

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        return data

    def apply(self, frame_rate: int, data: np.array) -> np.array:
        partial_result = data
        if self.inner_filter != None:
            partial_result = self.inner_filter.apply(frame_rate, data)

        return self.execute(frame_rate, partial_result)
