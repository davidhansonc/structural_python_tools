import os
from PIL import Image
import pillow_heif


def heic_to_jpg(heic_file_name, new_name):
    heif_file = pillow_heif.read_heif(heic_file_name)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    
    )

    image.save(f"./{new_name}.png", format("png"))


def multi_convert(directory):
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f) & filename.endswith("HEIC"):
            heic_to_jpg(f, filename.removesuffix(".HEIC"))