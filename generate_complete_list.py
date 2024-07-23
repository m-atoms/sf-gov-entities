import csv
import os

def read_csv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def write_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def process_files():
    # Read input files
    elected = read_csv('sf_gov_elected.csv')
    commissions = read_csv('sf_gov_commissions.csv')
    departments = read_csv('sf_gov_departments.csv')
    advisory = read_csv('sf_gov_advisory.csv')

    # Prepare output data
    output = [['Elected', 'Elected, Legal Source', 'Commissions', 'Commissions, Legal Source', 
               'Department Heads', 'Departments', 'Departments, Legal Source', 'Advisory', 'Advisory, Legal Source']]

    # Process each file and add to output
    max_rows = max(len(elected), len(commissions), len(departments), len(advisory))

    for i in range(1, max_rows):  # Skip headers
        row = [''] * 9  # Initialize empty row

        if i < len(elected):
            row[0] = elected[i][0]
            row[1] = elected[i][1]

        if i < len(commissions):
            row[2] = commissions[i][0]
            row[3] = commissions[i][1]

        if i < len(departments):
            row[4] = departments[i][0]
            row[5] = departments[i][1]
            row[6] = departments[i][2]

        if i < len(advisory):
            row[7] = advisory[i][0]
            row[8] = advisory[i][1]

        output.append(row)

    # Write output file
    write_csv('sf_gov_entities.csv', output)

if __name__ == '__main__':
    process_files()
    print("sf_gov_entities.csv has been generated successfully.")
