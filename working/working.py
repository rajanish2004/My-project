import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Define the regex pattern for matching the time format
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Extract groups from regex match
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Provide default value for minutes if not present
    start_minute = start_minute if start_minute else "00"
    end_minute = end_minute if end_minute else "00"

    # Convert to integers
    start_hour, start_minute = int(start_hour), int(start_minute)
    end_hour, end_minute = int(end_hour), int(end_minute)

    # Validate hour and minute ranges
    if not (1 <= start_hour <= 12 and 0 <= start_minute < 60 and 1 <= end_hour <= 12 and 0 <= end_minute < 60):
        raise ValueError("Invalid time")

    # Convert to 24-hour format
    start_hour_24 = convert_to_24_hour(start_hour, start_minute, start_period)
    end_hour_24 = convert_to_24_hour(end_hour, end_minute, end_period)

    return f"{start_hour_24} to {end_hour_24}"

def convert_to_24_hour(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
