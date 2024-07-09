import sys
import csv

# Constants
EXPECTED_COLUMNS = ['name', 'house']
OUTPUT_COLUMNS = ['first', 'last', 'house']

def process_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != EXPECTED_COLUMNS:
                sys.exit(f"Expected columns {EXPECTED_COLUMNS} in {input_file}")

            rows = []
            for row in reader:
                full_name = row['name']
                last_name, first_name = full_name.split(", ")
                new_row = {
                    'first': first_name,
                    'last': last_name,
                    'house': row['house']
                }
                rows.append(new_row)

        with open(output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=OUTPUT_COLUMNS)
            writer.writeheader()
            writer.writerows(rows)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_csv(input_file, output_file)
    print(f"Conversion complete. Output written to {output_file}")

if __name__ == "__main__":
    main()
