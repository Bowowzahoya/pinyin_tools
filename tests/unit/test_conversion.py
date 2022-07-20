import pytest
from unit_context import pinyin_tools
from pinyin_tools import conversion

PINYIN_SENTENCES = ["nǐ hǎo ma",\
    "nǐ",\
    "",
    "NǏ HǍO MA?",
    "this is not all pīnyīn"]

LAZY_PINYIN_SENTENCES = ["ni hao ma",\
    "ni",
    "",
    "NI HAO MA?",
    "this is not all pinyin"]

EXTENDED_PINYIN_SENTENCES = ["nĭ hӑo",
    "lyù"]

EXTENDED_LAZY_PINYIN_SENTENCES = ["ni hao",
    "lyu"]


@pytest.mark.parametrize("sentence", LAZY_PINYIN_SENTENCES)
def test_lazify_lazified_pinyin(sentence):
    lazified_sentence = conversion.lazify(sentence)
    assert lazified_sentence == sentence

@pytest.mark.parametrize("sentence,lazy_sentence", list(zip(PINYIN_SENTENCES, LAZY_PINYIN_SENTENCES)))
def test_lazify_pinyin(sentence, lazy_sentence):
    lazified_sentence = conversion.lazify(sentence)
    assert lazified_sentence == lazy_sentence

@pytest.mark.parametrize("sentence,lazy_sentence", list(zip(EXTENDED_PINYIN_SENTENCES, EXTENDED_LAZY_PINYIN_SENTENCES)))
def test_lazify_pinyin_extended(sentence, lazy_sentence):
    lazified_sentence = conversion.lazify(sentence, mode="extended")
    assert lazified_sentence == lazy_sentence
