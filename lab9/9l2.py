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
from PIL import Image, ImageFilter
import os
from pathlib import Path


input_folder = Path("input_images")
output_folder = Path("output_images")


output_folder.mkdir(parents=True, exist_ok=True)


allowed_extensions = {'.jpg', '.jpeg', '.png'}


for img_path in input_folder.iterdir():
    if img_path.suffix.lower() in allowed_extensions:
        try:

            img = Image.open(img_path)

            filtered_img = img.filter(ImageFilter.CONTOUR)

            output_path = output_folder / img_path.name
            filtered_img.save(output_path)
            print(f"Обработан файл: {img_path.name}")
        except Exception as e:
            print(f"Не удалось обработать файл {img_path.name}: {e}")

print("Обработка завершена.")