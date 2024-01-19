import os
import re

def remove_spaces(directory):
    for filename in os.listdir(directory):
        if ' ' in filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace(' ', '')))

# Ask for user input for the directory path
directory_path = input("Please enter the directory path: ")
remove_spaces(directory_path)


def remove_extra_zeros_and_round(directory):
    for filename in os.listdir(directory):
        # Find decimal numbers in the filename
        matches = re.findall(r'\d+\.\d+', filename)
        for match in matches:
            # Round to 3 decimal places, remove trailing zeros and replace in filename
            new_match = '{0:g}'.format(round(float(match), 3))
            filename = filename.replace(match, new_match)
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename))

# Usage
remove_extra_zeros_and_round("/path/to/your/directory")