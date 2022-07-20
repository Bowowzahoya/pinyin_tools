import pytest
from unit_context import pinyin_tools
from pinyin_tools import identify

SENTENCES = ["xiange",
    "xi'ange",
    "xia'nge",
    "nǐ hǎo ma",
    "",
    "NǏ HǍO MA?",
    "this is not all pīnyīn",
    "this is not all pinyin",
    ".ni, hao ma",
    "NI HAO MA?",
    "nĭ hӑo",
    "lyu",
    "lyù"]

OUTCOMES_LAZY_MODE = [True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False]

OUTCOMES_EXTENDED_MODE = [True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    True,
    False]

OUTCOMES_TONES_MODE = [True,
    True,
    False,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    False,
    False,
    False]

OUTCOMES_TONES_EXTENDED_MODE = [True,
    True,
    False,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    False,
    True,
    True]

@pytest.mark.parametrize("sentence,desired_outcome", list(zip(SENTENCES, OUTCOMES_LAZY_MODE)))
def test_is_allowed_pinyin_lazy_mode(sentence, desired_outcome):
    outcome = identify.is_pinyin(sentence)
    assert outcome == desired_outcome

@pytest.mark.parametrize("sentence,desired_outcome", list(zip(SENTENCES, OUTCOMES_EXTENDED_MODE)))
def test_is_allowed_pinyin_extended_mode(sentence, desired_outcome):
    outcome = identify.is_pinyin(sentence, mode="extended")
    assert outcome == desired_outcome

@pytest.mark.parametrize("sentence,desired_outcome", list(zip(SENTENCES, OUTCOMES_TONES_MODE)))
def test_is_allowed_pinyin_tones_mode(sentence, desired_outcome):
    outcome = identify.is_pinyin(sentence, mode="tones")
    assert outcome == desired_outcome

@pytest.mark.parametrize("sentence,desired_outcome", list(zip(SENTENCES, OUTCOMES_TONES_EXTENDED_MODE)))
def test_is_allowed_pinyin_tones_extended_mode(sentence, desired_outcome):
    outcome = identify.is_pinyin(sentence, mode="tones_extended")
    assert outcome == desired_outcome