from PIL import Image

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        resized_img = img.resize(size, Image.LANCZOS)
        resized_img.save(output_path)

input_image_path = 'input.jpg'
output_image_path = 'output.png'
new_size = (1200, 400)

resize_image(input_image_path, output_image_path, new_size)
