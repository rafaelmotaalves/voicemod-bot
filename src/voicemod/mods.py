from voicemod.filters import VolumeFilter, PitchShiftFilter, ReverbFilter, WhaleFilter, ReverseFilter, BandPassFilter, NoiseFilter
from voicemod.io import read, write

mods = {
    "luan_gameplays": VolumeFilter(volume=5),
    "alvin": PitchShiftFilter(steps=8),
    "darth_vader": PitchShiftFilter(steps=-5),
    "eco": ReverbFilter(delay=200, decay=0.6),
    "baleies": PitchShiftFilter(WhaleFilter(rate=0.3), steps=-1),
    "reverse": ReverseFilter(),
    "radio": VolumeFilter(NoiseFilter(BandPassFilter(order=6, low=300, high=3000), density=100), volume=1.5)
}

def list_mods():
    return mods.keys()

def apply_mod(audio_path, mod_name):
    frame_rate, file = read(audio_path)

    if mod_name in mods:
        mod = mods[mod_name]
        write(audio_path, mod.apply(frame_rate, file), frame_rate)

    return audio_path
