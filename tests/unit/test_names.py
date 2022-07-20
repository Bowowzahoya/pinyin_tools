import pytest
from unit_context import pinyin_tools
from pinyin_tools import names

last_nameS = ["ge", \
    "xi'an",
    "xian",
    "zhu ge",
    "zhug e",
    None]

FIRST_NAMES = ["ge",
    "xiuquan",
    "mamahuhu",
    "manao",
    "john"]

last_nameS_OUTCOMES = [True,
    False,
    True,
    True,
    False,
    False]

FIRST_NAMES_OUTCOMES = [True,
    True,
    False,
    True,
    False]

NAMES = ["ouyang lili",
    "mouyang lili",
    "lili",
    "xian",
    "xi'anlulu",
    "xianlulu"]

NAMES_OUTCOMES = [True,
    False,
    True,
    True,
    False,
    True]


@pytest.mark.parametrize("name,desired_outcome", list(zip(last_nameS, last_nameS_OUTCOMES)))
def test_is_sirname(name, desired_outcome):
    outcome = names.is_last_name(name)
    assert outcome == desired_outcome

@pytest.mark.parametrize("name,desired_outcome", list(zip(FIRST_NAMES, FIRST_NAMES_OUTCOMES)))
def test_is_first_name(name, desired_outcome):
    outcome = names.is_first_name(name)
    assert outcome == desired_outcome

@pytest.mark.parametrize("name,desired_outcome", list(zip(NAMES, NAMES_OUTCOMES)))
def test_is_name(name, desired_outcome):
    outcome = names.is_name(name)
    assert outcome == desired_outcome
