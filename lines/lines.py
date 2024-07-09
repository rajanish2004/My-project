import sys
import os

def count_lines_of_code(file_path):
    if not file_path.endswith('.py'):
        sys.exit("Not a Python file")

    if not os.path.isfile(file_path):
        sys.exit("File does not exist")

    loc = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()  # Strip leading and trailing whitespace
            if line == '' or line.startswith('#'):
                continue  # Ignore blank lines and lines that are comments
            loc += 1

    return loc

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]

    loc = count_lines_of_code(file_path)
    print(loc)

if __name__ == "__main__":
    main()
