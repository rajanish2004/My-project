import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Regular expression to match "um" as a standalone word, case-insensitively
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
