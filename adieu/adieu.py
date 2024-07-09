import sys

def bid_adieu(names):
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        # More than two names
        # Join all names with commas except the last two with "and"
        farewell_message = "Adieu, adieu, to "
        farewell_message += ", ".join(names[:-2]) + ", "
        farewell_message += names[-2] + ", and " + names[-1]
        print(farewell_message)

def main():
    names = []

    print("Enter names (one per line, Ctrl+D to end):")

    # Read names until EOF (Ctrl+D)
    for line in sys.stdin:
        name = line.strip()
        if name:
            names.append(name)

    # Bid adieu
    bid_adieu(names)

if __name__ == "__main__":
    main()
