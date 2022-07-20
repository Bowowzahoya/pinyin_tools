from .constants import *

def lazify(string, nan_value=None, mode=NORMAL_MODE):
    """
    Removes tones from a pinyin string
    """
    if string in [None,"", npnan]:
        if nan_value is None: return string
        else: return nan_value

    if mode == NORMAL_MODE: tones_dictionary = TONES_DICTIONARY
    elif mode == EXTENDED_MODE: tones_dictionary = TONES_DICTIONARY_EXTENDED
    
    for char in tones_dictionary.keys():
        char_with_tone_versions = tones_dictionary[char]

        for char_with_tone in char_with_tone_versions:
            string = string.replace(char_with_tone, char)
            string = string.replace(char_with_tone.upper(),char.upper())
            
    return string