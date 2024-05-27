from PIL import Image, ImageFilter
import os
from pathlib import Path

input_folder = Path("input_images")
output_folder = Path("output_images")

output_folder.mkdir(parents=True, exist_ok=True)

for img_name in input_folder.glob("*.jpg"):

    img = Image.open(img_name)

    filtered_img = img.filter(ImageFilter.CONTOUR)

    output_path = output_folder / img_name.name
    filtered_img.save(output_path)

print("Обработка завершена.")
