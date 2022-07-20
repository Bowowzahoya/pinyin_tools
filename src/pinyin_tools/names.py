from .splitting import split
from .constants import *

def is_last_name(name, mode=LAZY_MODE):
    if name in NAN_VALUES or not isinstance(name, str):
        return False

    split_possibilities = split(name, mode=mode)

    if any([len(split_possibility) == 1 for split_possibility in split_possibilities]):
        return True
    elif any([split_possibility in TWO_HANZI_FAMILY_NAMES for split_possibility in split_possibilities]):
        return True
    else:
        return False

def is_first_name(name, mode=LAZY_MODE):
    if name in NAN_VALUES or not isinstance(name, str):
        return False

    split_possibilities = split(name, mode=mode)

    if any([len(split_possibility) in (1, 2) for split_possibility in split_possibilities]):
        return True
    else:
        return False

def is_name(name, mode=LAZY_MODE, in_order=False):
    if name in NAN_VALUES or not isinstance(name, str):
        return False

    split_possibilities = split(name, mode=mode)

    if not any([len(split_possibility) in NAME_LENGTH_POSSIBILITIES for split_possibility in split_possibilities]):
        return False
    else:
        for split_possibility in split_possibilities:
            name_part_1 = "'".join(split_possibility[:1])
            name_part_2 = "'".join(split_possibility[1:])
            if is_last_name(name_part_1) and is_first_name(name_part_2):
                return True
            if is_first_name(name_part_1) and is_last_name(name_part_2):
                return True
            
            if len(split_possibility) > 2:
                name_part_1 = "'".join(split_possibility[:2])
                name_part_2 = "'".join(split_possibility[2:])
                if is_last_name(name_part_1) and is_first_name(name_part_2):
                    return True
                if is_first_name(name_part_1) and is_last_name(name_part_2):
                    return True
        return False # if no match found


