import os
import shutil
import ffmpeg
from wand.image import Image

def convert_heic_to_png(directory):
    # Define the path for the new directory for original HEIC images
    original_heic_dir = os.path.join(directory, "original heic images")
    
    # Create a new directory for original HEIC images if it doesn't exist
    os.makedirs(original_heic_dir, exist_ok=True)
    print("Created directory for original HEIC images.")

    # Check if there are any HEIC files in the directory
    heic_files = [f for f in os.listdir(directory) if f.lower().endswith(".heic")]
    if not heic_files:
        print("No HEIC files to convert.")
        return
    
    # Loop through all HEIC files in the directory
    for filename in heic_files:
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
            print(f"Error processing {filename}: {e}")

    print("HEIC to PNG conversion process completed.")

def convert_hevc_to_mp4(input_file, output_file):
    # Define the directory for original HEVC videos
    original_hevc_dir = os.path.join(os.path.dirname(input_file), "original hevc files")
    os.makedirs(original_hevc_dir, exist_ok=True)

    try:
        # Set up the conversion command line
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file, vcodec='libx264', acodec='copy')
        ffmpeg.run(stream)
        print(f"Conversion successful! Converted file saved to {output_file}")

        # Move the original HEVC file to the designated directory
        shutil.move(input_file, os.path.join(original_hevc_dir, os.path.basename(input_file)))
        print(f"Moved original HEVC file to {original_hevc_dir}")

    except Exception as e:
        print(f"Error converting HEVC file: {e}")

if __name__ == "__main__":
    try:
        directory = input("Enter the directory path for HEIC files: ")
        if not os.path.exists(directory):
            raise ValueError("The specified directory does not exist.")
        convert_heic_to_png(directory)
    except Exception as e:
        print(f"An error occurred during HEIC conversion: {e}")

    try:
        input_hevc_video = input("Enter the path of the HEVC file to convert: ")
        output_mp4_video = os.path.join(os.path.dirname(input_hevc_video), "output_video.mp4")
        convert_hevc_to_mp4(input_hevc_video, output_mp4_video)
    except Exception as e:
        print(f"An error occurred during HEVC conversion: {e}")
