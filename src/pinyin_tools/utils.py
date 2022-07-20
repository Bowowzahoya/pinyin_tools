from .constants import *

def get_allowed_syllables(mode):
    if mode == LAZY_MODE: allowed_syllables = ALLOWED_SYLLABLES
    elif mode == EXTENDED_MODE: allowed_syllables = ALLOWED_SYLLABLES_EXTENDED
    elif mode == TONES_MODE: allowed_syllables = ALLOWED_SYLLABLES_WITH_TONES
    elif mode == TONES_EXTENDED_MODE: allowed_syllables = ALLOWED_SYLLABLES_WITH_TONES_EXTENDED
    else: raise ValueError(f"Mode '{mode}' not allowed.")
    return allowed_syllables