import pytest
from bank import value

def test_hello_case_insensitive():
    assert value("Hello World") == 0
    assert value("HELLO everyone") == 0
    assert value("hello") == 0
    assert value("hELLo, how are you?") == 0

def test_starts_with_h():
    assert value("hi there") == 20
    assert value("Holidays are coming!") == 20
    assert value("H") == 20

def test_other_cases():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
    assert value("Goodbye") == 100

# Additional tests can be added to cover edge cases, etc.

if __name__ == "__main__":
    pytest.main()
