import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define the regular expression for an iframe YouTube URL
    pattern = r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    # If a match is found, return the shorter URL
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()
