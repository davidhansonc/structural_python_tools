import os
from PIL import Image
import pillow_heif
import shutil


def copy_file_to_folder(source_file, target_folder):
    try:
        # Copy the file to the target folder
        shutil.copy(source_file, target_folder)
        print(f"File '{source_file}' successfully copied to '{target_folder}'.")
    except FileNotFoundError:
        print("The source file does not exist.")
    except PermissionError:
        print("Permission denied. Unable to copy the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def heic_to_png(heic_file_name, new_name):
    heif_file = pillow_heif.read_heif(heic_file_name)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    image.save(f"./converts/{new_name}.png", format("png"))


def multi_convert(directory):
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) & filename.endswith("HEIC"):
            heic_to_png(f, filename.removesuffix(".HEIC"))
        # moving movie files to the converts folder without modification
        elif os.path.isfile(f) & filename.endswith(".MOV"):
            source_file_path = f'./{filename}'
            target_folder_path = './converts/'
            copy_file_to_folder(source_file_path, target_folder_path)


if __name__ == '__main__':
    folder_name = "./converts"
    if not os.path.exists(folder_name):
        # Create the folder
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    single_or_multi = input("'single' file or 'directory' of files? ")
    if single_or_multi == "single":
        heic = input("heic file name: ") #enter without quotes
        new_name = input("new name (without extension): ") #enter without quotes
        heic_to_png(heic, new_name)
        print("done!")
    
    elif single_or_multi == "directory":
        directory = input("directory of photos: ")  #enter path without quotes.
        multi_convert(directory)
        print("done!")
    else:
        print("error!")