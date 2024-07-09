import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("not an integer")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(20)  # Exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(-1)  # Negative deposit
    with pytest.raises(ValueError):
        jar.deposit("not an integer")

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(10)  # More than available cookies
    with pytest.raises(ValueError):
        jar.withdraw(-1)  # Negative withdrawal
    with pytest.raises(ValueError):
        jar.withdraw("not an integer")

if __name__ == "__main__":
    pytest.main()
