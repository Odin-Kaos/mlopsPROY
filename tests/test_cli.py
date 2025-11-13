# test_logic.py
import pytest
import math
from src.preprocessing import (
    remove_missing, fill_missing, remove_duplicates,
    normalize_minmax, standardize_zscore, clip_values,
    convert_to_int, log_transform, tokenize_text,
    clean_text, remove_stopwords, flatten_list, shuffle_list
)

@pytest.fixture
def sample_numbers():
    return [10, 20, 30]

@pytest.fixture
def sample_text():
    return "Hello World!! 123"

@pytest.mark.parametrize("values,expected", [
    ([1, None, "", float("nan"), 2], [1, 2]),
    ([None, "", float("nan")], []),
    ([1, 2, 3], [1, 2, 3]),
])
def test_remove_missing(values, expected):
    assert remove_missing(values) == expected

@pytest.mark.parametrize("values,fill_value,expected", [
    ([1, None, 2, ""], 0, [1, 0, 2, 0]),
    ([None, float("nan")], 99, [99, 99]),
])
def test_fill_missing(values, fill_value, expected):
    assert fill_missing(values, fill_value) == expected
