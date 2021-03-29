from voicemod.filters import VolumeFilter
from voicemod.io import read, write

mods = {
    "volume_down": VolumeFilter(volume=0.5),
    "volume_up": VolumeFilter(volume=2)
}

def apply_mod(audio_path, mod_name):
    frame_rate, file = read(audio_path)
    
    if mod_name in mods:
        mod = mods[mod_name]
        write(audio_path, mod.apply(frame_rate, file))
    
    return audio_path