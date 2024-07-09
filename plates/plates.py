def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # The first number used cannot be a '0'
    has_letter = False
    for c in s:
        if c.isalpha():
            has_letter = True
        elif c.isdigit():
            if c == '0' and has_letter == False:
                return False
            has_letter = False
        else:
            return False

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in [',', ' ', '!', '?']:
            return False

    # If we pass all the tests, return True
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()
