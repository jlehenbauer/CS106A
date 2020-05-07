from simpleimage import SimpleImage


def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_size pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_size is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_size pixels shaved off each
        side of the original image
    """
    # TODO: your code here
    pass


if __name__ == '__main__':
    main()