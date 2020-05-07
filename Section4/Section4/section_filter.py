from simpleimage import SimpleImage


def main():
    """
    This program loads an image and applies the narok filter
    to it by setting "bright" pixels to grayscale values.
    """
    image = SimpleImage('images/simba-sq.jpg')

    # TODO: your code here

    image.show()


if __name__ == '__main__':
    main()