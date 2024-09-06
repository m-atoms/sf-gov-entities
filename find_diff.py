import csv
import sys
from collections import defaultdict

def get_unique_values(file_path, column_name):
    unique_values = set()
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        if column_name not in reader.fieldnames:
            print(f"Error: Column '{column_name}' not found in {file_path}")
            print(f"Available columns: {reader.fieldnames}")
            sys.exit(1)
        for row in reader:
            unique_values.add(row[column_name])
    return unique_values

def print_columns(left_column, right_column, left_title, right_title):
    max_left_width = max(len(left_title), max(len(str(item)) for item in left_column), 1)
    max_right_width = max(len(right_title), max(len(str(item)) for item in right_column), 1)

    print(f"{left_title:<{max_left_width}} | {right_title:<{max_right_width}}")
    print("-" * (max_left_width + max_right_width + 3))

    for left, right in zip(left_column, right_column):
        print(f"{str(left):<{max_left_width}} | {str(right):<{max_right_width}}")
        if str(left) == "":
            break

def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py <csv1_path> <csv1_column> <csv2_path> <csv2_column>")
        sys.exit(1)

    csv1_path, csv1_column, csv2_path, csv2_column = sys.argv[1:]

    csv1_values = get_unique_values(csv1_path, csv1_column)
    csv2_values = get_unique_values(csv2_path, csv2_column)

    unique_to_csv1 = sorted(csv1_values - csv2_values)
    unique_to_csv2 = sorted(csv2_values - csv1_values)
    common_values = sorted(csv1_values.intersection(csv2_values))

    max_length = max(len(unique_to_csv1), len(unique_to_csv2), len(common_values))
    padded_unique_to_csv1 = unique_to_csv1 + [''] * (max_length - len(unique_to_csv1))
    padded_unique_to_csv2 = unique_to_csv2 + [''] * (max_length - len(unique_to_csv2))
    padded_common_values = common_values + [''] * (max_length - len(common_values))

    print(f"\nUnique values in {csv1_path} ({csv1_column}) vs {csv2_path} ({csv2_column}):")
    print_columns(padded_unique_to_csv1, padded_unique_to_csv2, csv1_column, csv2_column)

    #print(f"\nCommon values:")
    #for value in common_values:
    #    print(value)

if __name__ == "__main__":
    main()
