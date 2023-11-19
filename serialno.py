"""
Purpose of the code is to get a temp serial number and a newly created serial number and append it to a master file.

This has to be added to the final QC step for Wave DX, Wave 3 and Stream Decks
"""

import os
import csv

def get_desktop_path():
    # Get the path to the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    return desktop_path

# Function to read string from CSV file on the desktop
def read_serial(file_name):

    with open(file_name, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Assuming the CSV file has only one row and one column
        for row in csv_reader:
            if len(row) > 0:
                string_from_csv = row[0]
                return string_from_csv
            else:
                print("CSV file is empty or does not contain any data.")
                return None
    csv_file.close()

file_name_temp = r'C:\temp_serialno.csv'
file_name_new = r'C:\new_serialno.csv'

append_file=r'C:\masterserial.csv'


temp_serial = read_serial(file_name_temp)
new_serial = read_serial(file_name_new)


with open(append_file, 'a', newline='') as csv_output_file:
            csv_output_file.write(temp_serial + ',' + new_serial + '\n')
csv_output_file.close()