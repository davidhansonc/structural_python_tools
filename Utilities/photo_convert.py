import os
import shutil
import ffmpeg
from wand.image import Image

def convert_heic_to_png(heic_path, png_path):
    try:
        with Image(filename=heic_path) as img:
            img.format = 'png'
            img.save(filename=png_path)
            print(f"Converted {os.path.basename(heic_path)} to PNG.")
        return True
    except Exception as e:
        print(f"Error processing {os.path.basename(heic_path)}: {e}")
        return False

def convert_hevc_to_mp4(input_path, output_path):
    try:
        print(f"Attempting to convert: {input_path} to {output_path}")
        stream = ffmpeg.input(input_path)
        stream = ffmpeg.output(stream, output_path, vcodec='libx264', acodec='copy')
        ffmpeg.run(stream)
        print(f"Converted {os.path.basename(input_path)} to MP4.")
        return True
    except Exception as e:
        print(f"Error converting {os.path.basename(input_path)}: {e}")
        return False

if __name__ == "__main__":
    try:
        directory = input("Enter the directory path for files: ")
        if not os.path.exists(directory):
            raise ValueError("The specified directory does not exist.")
        originals_dir = os.path.join(directory, "original images")
        os.makedirs(originals_dir, exist_ok=True)
        print("Created directory for original images.")

        heic_files = [f for f in os.listdir(directory) if f.lower().endswith(".heic")]
        for filename in heic_files:
            heic_path = os.path.join(directory, filename)
            png_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.png")
            if convert_heic_to_png(heic_path, png_path):
                shutil.move(heic_path, os.path.join(originals_dir, filename))
                print(f"Moved {filename} to 'original images' directory.")

        mov_files = [f for f in os.listdir(directory) if f.lower().endswith(".mov")]
        for filename in mov_files:
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.mp4")
            if convert_hevc_to_mp4(input_path, output_path):
                shutil.move(input_path, os.path.join(originals_dir, filename))
                print(f"Moved {filename} to 'original images' directory.")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
