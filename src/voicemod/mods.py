from voicemod.filters import VolumeFilter, PitchShiftFilter
from voicemod.io import read, write

mods = {
    "luan_gameplays": VolumeFilter(volume=5),
    "alvin": PitchShiftFilter(steps=8),
    "darth_vader": PitchShiftFilter(steps=-5)
}

def apply_mod(audio_path, mod_name):
    frame_rate, file = read(audio_path)
    
    if mod_name in mods:
        mod = mods[mod_name]
        write(audio_path, mod.apply(frame_rate, file), frame_rate)
    
    return audio_path