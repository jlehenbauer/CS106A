from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    # original_image:
    # - .height
    # - .width
    # - .pixel

    # original_img.show()

    # Get height and width of original
    old_height = original_img.height
    old_width = original_img.width

    # Make a new image with new width and height
    new_height = old_height + 2 * border_size
    new_width = old_width + 2 * border_size

    new_image = SimpleImage.blank(new_height, new_width, "red")

    """
    for pixel in new_image:
        pixel.red = 0
        pixel.blue = 0
        pixel.green = 0
    """

    for x in range(border_size + 1, old_width + border_size):
        for y in range(border_size + 1, old_height + border_size):
            old_pixel = original_img.get_pixel(x - border_size, y - border_size)
            new_image.set_pixel(x, y, old_pixel)

    return new_image


if __name__ == '__main__':
    main()