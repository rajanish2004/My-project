import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_multiple_um():
    assert count("um, thanks, um...") == 2
    assert count("Um, thanks, um...") == 2

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("Um!") == 1

def test_um_in_words():
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_no_um():
    assert count("hello world") == 0

if __name__ == "__main__":
    pytest.main()
