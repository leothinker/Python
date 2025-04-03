from PIL import Image


def resize_image(input_path, output_path, size):
    """
    Resize an image to the specified size.

    :param input_path: str, path to the input image
    :param output_path: str, path to save the resized image
    :param size: tuple, new size in the format (width, height)
    """
    with Image.open(input_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)
        print(f"Image saved to {output_path} with size {size}")


# Example usage
resize_image("20220809173613_fe988.jpeg", "output_image.jpg", (100, 100))
