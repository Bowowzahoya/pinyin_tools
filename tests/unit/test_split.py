import pytest
from unit_context import pinyin_tools
from pinyin_tools import splitting

WORDS = ["pinyin", \
    "liange",
    "lian'ge",
    None]

SPLIT_WORDS = [set([("pin", "yin")]),
    set([("li", "ang", "e"), ("lian", "ge"), ("liang", "e"), ("li", "an", "ge")]),
    set(),
    set()]

SPLIT_WORDS_WITH_DELIMITERS = [set([("pin", "yin")]),
    set([("li", "ang", "e"), ("lian", "ge"), ("liang", "e"), ("li", "an", "ge")]),
    set([("lian", "ge"), ("li", "an", "ge")]),
    set()]


@pytest.mark.parametrize("word,desired_outcome", list(zip(WORDS, SPLIT_WORDS)))
def test_split_without_delimiters(word, desired_outcome):
    outcome = splitting.split_without_delimiters(word)
    assert outcome == desired_outcome

@pytest.mark.parametrize("word,desired_outcome", list(zip(WORDS, SPLIT_WORDS_WITH_DELIMITERS)))
def test_split_with_delimiters(word, desired_outcome):
    outcome = splitting.split(word)
    assert outcome == desired_outcome

