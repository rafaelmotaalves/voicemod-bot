import numpy as np

MAX_INT = 2147483647

def safe_cast_to_int32(value):
    try:
        return np.int32(value)
    except OverflowError:
        return np.int32(MAX_INT if value > 0 else -MAX_INT)
