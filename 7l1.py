from PIL import Image

img = Image.open('qwerty.jpg')
img.show()
print("Цветовая модель изображения:", img.mode)
print("Размер изображения:", img.size)
print("Формат изображения:", img.format)