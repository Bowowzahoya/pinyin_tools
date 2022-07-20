from .constants import *
from .utils import get_allowed_syllables

def _clean_and_divide_string(function):
    def _inner_function(string, **kwargs):
        if string in NAN_VALUES or not isinstance(string, str):
            return function(string, **kwargs)

        string = string.lower()
        for char in INTERPUNCTION_CHARACTERS:
            string = string.replace(char, " ")
        while "  " in string:
            string = string.replace("  ", " ")
        while string[0] == " " and len(string) > 0:
            string = string[1:]
        while string[-1] == " " and len(string) > 0:
            string = string[:-1]
        if len(string) == 0:
            return function(string, **kwargs)

        return all([function(sub_string, **kwargs) for sub_string in string.split(" ")])

    return _inner_function

@_clean_and_divide_string
def is_pinyin(string, mode=LAZY_MODE):
    """
    Checks if a string can be (lazy) pinyin or not, according to possible
    sounds in pinyin.
    """
    if string in NAN_VALUES or not isinstance(string, str):
        return False

    allowed_syllables = get_allowed_syllables(mode)
    
    # main body
    length_string = len(string)
    for syllable in allowed_syllables:
        length_syllable = len(syllable)
        if length_syllable <= length_string: 
        # only search if string long enough to save time
            if syllable == string[:length_syllable]:
            # ok this part at least is possible in pinyin, what is left?
                rest = string[length_syllable:]
                if rest == "":
                    return True
                else:
                    if is_pinyin(rest, mode=mode): return True
    
    # only return False if checked all options
    return False



