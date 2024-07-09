import sys
import os
import csv
from tabulate import tabulate

def read_pizza_prices(file_path):
    if not file_path.endswith('.csv'):
        sys.exit("Not a CSV file")

    if not os.path.isfile(file_path):
        sys.exit("File does not exist")

    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)  # Read the header row
        rows = list(reader)    # Read all remaining rows

    return header, rows

def main():
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_path = sys.argv[1]

    header, rows = read_pizza_prices(file_path)

    # Format the table using tabulate
    table = tabulate(rows, headers=header, tablefmt='grid')

    print(table)

if __name__ == "__main__":
    main()
