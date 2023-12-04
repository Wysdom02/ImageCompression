from PIL import Image
import pillow_heif
from PIL import TiffImagePlugin


input_path="SOP/1920-1080-sample.tiff"
output_path_Jpeg = "SOP/1920.jpeg"
output_path_Heic= "SOP/1920.heif"


def convert_tif_to_jpeg(input_path, output_path):
    image = Image.open(input_path)
    image.convert("RGB").save(output_path, "JPEG")

def convert_tif_to_heic(input_path, output_path):
    pillow_heif.register_heif_opener()
    image = Image.open(input_path)
    # Uncomment below if image is in TIF format
    exif = image.getexif()
    del exif[TiffImagePlugin.STRIPOFFSETS]
    image.save(output_path)
    image.close()



convert_tif_to_jpeg(input_path, output_path_Jpeg)
convert_tif_to_heic(input_path, output_path_Heic)

import numpy as np
from pillow_heif import register_heif_opener

register_heif_opener()

def calculate_rmse(image_path1, image_path2):
    # Open images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Convert images to NumPy arrays
    array1 = np.array(image1)
    array2 = np.array(image2)

    # Ensure both arrays have the same shape
    if array1.shape != array2.shape:
        raise ValueError("Images must have the same dimensions.")

    # Calculate squared differences
    squared_diff = (array1 - array2) ** 2

    # Calculate mean of squared differences
    mean_squared_diff = np.mean(squared_diff)

    # Take the square root to get RMSE
    rmse = np.sqrt(mean_squared_diff)

    return rmse


rmse_value_heif = calculate_rmse(input_path, output_path_Heic)
rmse_value_jpeg = calculate_rmse(input_path, output_path_Jpeg)

print(f"Root Mean Square Error (RMSE) of HEIF image: {rmse_value_heif}")
print(f"Root Mean Square Error (RMSE)of jpg image : {rmse_value_jpeg}")
