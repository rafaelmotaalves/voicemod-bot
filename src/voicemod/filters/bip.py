from voicemod.filters.base import BaseFilter
from voicemod.io import read
import numpy as np
from pydub import AudioSegment
import logging
from voicemod.util import create_segment

class BipFilter(BaseFilter):
    def __init__(self, inner_filter):
        self.start_bip = AudioSegment.from_file("./assets/start-beep.wav")
        self.end_bip = AudioSegment.from_file("./assets/end-beep.wav")
        super().__init__(inner_filter)

    def execute(self, frame_rate: int, data: np.array) -> np.array:
        start_bip_copy = self.start_bip
        end_bip_copy = self.end_bip


        logging.log(0, start_bip_copy.frame_rate)
        logging.log(0, frame_rate)
        res =  start_bip_copy + create_segment(data, frame_rate) + end_bip_copy

        return res.get_array_of_samples()