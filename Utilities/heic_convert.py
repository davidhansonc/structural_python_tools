import os
import shutil
from wand.image import Image

def convert_heic_to_png(directory):
    # Define the path for the new directory for original HEIC images
    original_heic_dir = os.path.join(directory, "original heic images")
    
    # Create a new directory for original HEIC images if it doesn't exist
    os.makedirs(original_heic_dir, exist_ok=True)
    print("Created directory for original HEIC images.")

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.png")
            
            try:
                # Convert HEIC to PNG
                with Image(filename=heic_path) as img:
                    img.format = 'png'
                    img.save(filename=png_path)
                    print(f"Converted {filename} to PNG.")

                # Move the original HEIC file to the original HEIC images directory
                shutil.move(heic_path, os.path.join(original_heic_dir, filename))
                print(f"Moved {filename} to 'original heic images' directory.")

            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    # Print completion message
    print("All files processed.")

if __name__ == "__main__":
    try:
        directory = input("Enter the directory path: ")
        if not os.path.exists(directory):
            raise ValueError("The specified directory does not exist.")
        convert_heic_to_png(directory)
    except Exception as e:
        print(f"An error occurred: {e}")