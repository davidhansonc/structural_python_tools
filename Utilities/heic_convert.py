import os
from wand.image import Image

def convert_heic_to_jpg(directory):
    # Create a new directory for converted photos
    new_dir = os.path.join(directory, "converted_photos")
    os.makedirs(new_dir, exist_ok=True)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            # Convert HEIC to JPG
            with Image(filename=heic_path) as img:
                jpg_path = os.path.join(new_dir, f"{os.path.splitext(filename)[0]}.jpg")
                img.save(filename=jpg_path)

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    convert_heic_to_jpg(directory)
