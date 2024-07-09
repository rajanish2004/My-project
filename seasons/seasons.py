from datetime import date, datetime
import sys
from num2words import num2words

def main():
    birthdate_str = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        if birthdate > date.today():
            raise ValueError
    except ValueError:
        sys.exit("Invalid date format or future date")

    minutes = calculate_minutes(birthdate)
    minutes_in_words = number_to_words(minutes)
    print(f"You are {minutes_in_words} minutes old.")

def calculate_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    minutes = delta.days * 24 * 60
    return minutes

def number_to_words(number):
    return num2words(number).replace("-", " ").replace(",", "")

if __name__ == "__main__":
    main()
