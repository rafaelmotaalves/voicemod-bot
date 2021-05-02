from voicemod.filters import VolumeFilter, PitchShiftFilter, ReverbFilter, WhaleFilter, ReverseFilter, BandPassFilter, AddNoiseFilter, DynamicRangeCompress, BipFilter
from voicemod.io import read, write
from pydub import AudioSegment
from voicemod.util import create_segment

mods = {
    "luan_gameplays": VolumeFilter(volume=5),
    "alvin": PitchShiftFilter(steps=8),
    "darth_vader": PitchShiftFilter(steps=-5),
    "eco": ReverbFilter(delay=200, decay=0.6),
    "baleies": PitchShiftFilter(WhaleFilter(rate=0.3), steps=-1),
    "reverse": ReverseFilter(),
    "radio": VolumeFilter(AddNoiseFilter(BandPassFilter(order=6, low=300, high=3000), density=100), volume=1.5),
    "quality": DynamicRangeCompress()
}

def list_mods():
    return mods.keys()

def apply_mod(audio_path, mod_name):
    frame_rate, file = read(audio_path)

    if mod_name in mods:
        mod = mods[mod_name]

        res = mod.apply(frame_rate, file)

        if mod_name == "radio":
            frame_rate, res = add_bip(frame_rate, res)
        write(audio_path, res, frame_rate)



    return audio_path


def add_bip(frame_rate, data):
    end_bip = AudioSegment.from_file("./assets/end-beep-48k.wav")
    end_bip.set_channels(1)

    res = create_segment(data, frame_rate) + end_bip

    return res.frame_rate, res.get_array_of_samples()
    