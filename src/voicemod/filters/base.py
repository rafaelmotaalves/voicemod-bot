import numpy as np

class BaseFilter:
    def __init__(self, inner_filter=None, **kwargs):
        self.inner_filter = inner_filter
        self.params = kwargs

    def execute(self, data: np.array) -> np.array :
        return data

    def apply(self, data: np.array) -> np.array:
        partial_result = data
        if self.inner_filter != None:
            partial_result = self.inner_filter.apply(data)

        return self.execute(partial_result)
