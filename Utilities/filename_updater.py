import os

def remove_spaces(directory):
    for filename in os.listdir(directory):
        if ' ' in filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace(' ', '')))

# Ask for user input for the directory path
directory_path = input("Please enter the directory path: ")
remove_spaces(directory_path)
