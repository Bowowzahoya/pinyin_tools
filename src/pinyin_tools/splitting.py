from .constants import *
from .utils import get_allowed_syllables

import re


def split(word, mode=LAZY_MODE):
    if word in NAN_VALUES or not isinstance(word, str):
        return set()
        
    if mode in [LAZY_MODE, TONES_MODE]:
        delimiters_pattern = DELIMITERS_PATTERN
    elif mode in [EXTENDED_MODE, TONES_EXTENDED_MODE]:
        delimiters_pattern = DELIMITERS_EXTENDED_PATTERN

    split_word = re.split(delimiters_pattern, word)

    if len(split_word) <= 1:
        return split_without_delimiters(word, mode=mode)
    else:
        first_segment = split_word[0]
        rest_of_word = "'".join(split_word[1:])
        
        split_possibilities_first_segment = split_without_delimiters(first_segment, mode=mode)
        if len(split_possibilities_first_segment) == 0:
            return set()
        else:
            split_possibilities_rest_of_word = split(rest_of_word, mode=mode)
            if len(split_possibilities_rest_of_word) == 0:
                return set()

            split_possibilities = set()
            for split_possibility_first_segment in split_possibilities_first_segment:
                for split_possibility_rest_of_word in split_possibilities_rest_of_word:
                    split_possibilities.add(split_possibility_first_segment+split_possibility_rest_of_word)
            return split_possibilities

def split_without_delimiters(word, mode=LAZY_MODE):
    if word in NAN_VALUES or not isinstance(word, str):
        return set()

    allowed_syllables = get_allowed_syllables(mode)

    split_possibilities = set()
    for syllable in allowed_syllables:
        if syllable in word[:len(syllable)]:
            tentative_first_split = (syllable,)
            rest_of_word = word[len(syllable):]

            if len(rest_of_word) == 0:
                split_possibilities.add(tentative_first_split)
            else:
                split_possibilities_rest_of_word = split_without_delimiters(rest_of_word, mode=mode)
                if len(split_possibilities_rest_of_word) > 0:
                    # rest of word can be split
                    for split_possibility_rest_of_word in split_possibilities_rest_of_word:
                        split_possibilities.add(tentative_first_split+split_possibility_rest_of_word)
                else:
                    # rest of word can't be split
                    continue

    return split_possibilities
        