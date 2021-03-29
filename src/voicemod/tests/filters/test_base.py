import numpy as np

from voicemod.filters.base import BaseFilter


class DummyFilter(BaseFilter):
    def execute(self, frame_rate: int, data: np.array) -> np.array:
        f = np.vectorize(lambda x: x * 2)

        return f(data)


def test_init():
    test_filter = DummyFilter()
    filter = BaseFilter(test_filter, number=1, string="string")

    assert filter.params.get("string") == "string"
    assert filter.params.get("number") == 1
    assert filter.inner_filter == test_filter


def test_chaining():
    filter = DummyFilter(DummyFilter(DummyFilter()))

    result = filter.apply(1, np.array([1, 1, 1, 1]))

    assert np.all(result == 8)


def test_independent_parameters():
    filter = DummyFilter(DummyFilter(value=2), value=1, param=3)

    assert filter.params.get('value') == 1
    assert filter.params.get('param') == 3
    assert filter.inner_filter.params.get('value') == 2
