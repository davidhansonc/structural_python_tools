import os
import shutil
from wand.image import Image

def convert_heic_to_jpg(directory):
    # Define the path for the new directory for converted images
    new_dir = os.path.join(directory, "converted_images")
    
    # Check if the directory already exists. If yes, delete it.
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
        print("Deleted existing directory of converted images.")
    
    # Create a new directory for converted images
    os.makedirs(new_dir, exist_ok=True)
    print("Created directory for converted images.")

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Convert filename to lowercase before checking the extension
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            # Convert HEIC to JPG
            try:
                with Image(filename=heic_path) as img:
                    jpg_path = os.path.join(new_dir, f"{os.path.splitext(filename)[0]}.jpg")
                    img.save(filename=jpg_path)
            except Exception as e:
                print(f"Error converting {filename}: {e}")

    # Print completion message
    print("Conversions completed.")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    convert_heic_to_jpg(directory)
