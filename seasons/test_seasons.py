import pytest
from datetime import date
from unittest.mock import patch

from seasons import calculate_minutes, number_to_words

def test_calculate_minutes():
    with patch('seasons.date') as mock_date:
        mock_date.today.return_value = date(2024, 7, 8)
        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        delta = date(2024, 7, 8) - date(2020, 1, 1)
        assert calculate_minutes(date(2020, 1, 1)) == delta.days * 24 * 60

        delta = date(2024, 7, 8) - date(2022, 7, 1)
        assert calculate_minutes(date(2022, 7, 1)) == delta.days * 24 * 60

def test_number_to_words():
    assert number_to_words(525600) == "five hundred twenty five thousand six hundred"
    assert number_to_words(1440) == "one thousand four hundred forty"
    assert number_to_words(1) == "one"

if __name__ == "__main__":
    pytest.main()
