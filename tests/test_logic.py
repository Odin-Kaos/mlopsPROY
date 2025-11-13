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


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]

def test_normalize_minmax(sample_numbers):
    result = normalize_minmax(sample_numbers, 0, 1)
    assert min(result) == 0.0
    assert max(result) == 1.0

def test_standardize_zscore(sample_numbers):
    result = standardize_zscore(sample_numbers)
    assert pytest.approx(result.mean(), 0.01) == 0.0

def test_clip_values():
    assert clip_values([1, 5, 10], 2, 8) == [2, 5, 8]

def test_convert_to_int():
    assert convert_to_int(["1", "abc", "3.5"]) == [1]

def test_log_transform():
    assert log_transform([1, 10]) == [0.0, math.log(10)]

def test_tokenize_text(sample_text):
    assert tokenize_text(sample_text) == ["hello", "world", "123"]

def test_clean_text(sample_text):
    assert clean_text(sample_text) == "Hello World 123"

def test_remove_stopwords():
    assert remove_stopwords("this is a test", {"is", "a"}) == "this test"

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_shuffle_list(sample_numbers):
    result = shuffle_list(sample_numbers, seed=42)
    assert set(result) == set(sample_numbers)
