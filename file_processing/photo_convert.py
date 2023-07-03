import os
from PIL import Image
import pillow_heif


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

if __name__ == '__main__':
    single_or_multi = input("'single' file or 'directory' of files? ")
    if single_or_multi == "single":
        heic = input("heic file name: ")
        new_name = input("new name (without extension): ")
        heic_to_jpg(heic, new_name)
        print("done!")
    elif single_or_multi == "directory":
        directory = input("directory of photos: ")
        multi_convert(directory)
        print("done!")
    else:
        print("error!")