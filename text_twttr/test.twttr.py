import twttr
from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("Hello") == "Hll"

def test_shorten_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_no_vowels_in_string():
    assert shorten("Python") == "Pythn"

if __name__ == "__main__":
    twttr.main()
