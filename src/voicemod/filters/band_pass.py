import numpy as np
import math
from scipy.signal import butter, filtfilt
from voicemod.filters.base import BaseFilter

class BandPassFilter(BaseFilter):
    DEFAULT_CUTOFF = 3667
    DEFAULT_ORDER = 5

    def execute(self, frame_rate: int, data: np.array):
        low_cutoff = self.params.get("low", self.DEFAULT_CUTOFF)
        high_cutoff = self.params.get("high", self.DEFAULT_CUTOFF)
        order = self.params.get("order", self.DEFAULT_ORDER)
        
        numerator, denominator = self.butter_lowpass(low_cutoff, high_cutoff, frame_rate, order=order)
        return filtfilt(numerator, denominator, data)

    def butter_lowpass(self, low_cutoff: int, high_cutoff: int, frame_rate: int, order=5):
        lowcut = self.normalize_cutoff(frame_rate, low_cutoff)
        highcut = self.normalize_cutoff(frame_rate, high_cutoff)

        return butter(order, [lowcut, highcut], btype='band') 

    def normalize_cutoff(self, frame_rate: int, cutoff: int):
        nyquist_rate = 0.5 * frame_rate
        
        return cutoff / nyquist_rate