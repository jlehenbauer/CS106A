"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'
MODS = [
    [1.5, 0, 1.5],
    [.7, 1.2, 1.9],
    [1.2, .4, 0],
    [1, 1, 1],
    [0, 1.2, 1.2],
    [2, 2, 0]
]

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for mod in MODS:
        patch = make_recolored_patch(mod[0], mod[1], mod[2])
        final_image = attach_patch(patch, final_image, MODS.index(mod))

    final_image.show()


def attach_patch(patch, image, num):
    x_pos = (num % N_COLS) * PATCH_SIZE
    y_pos = (num // N_COLS) * PATCH_SIZE

    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            px = patch.get_pixel(x, y)
            image.set_pixel(x + x_pos, y + y_pos, px)

    return image


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)

    for px in patch:
        px.red *= red_scale
        px.green *= green_scale
        px.blue *= blue_scale

    return patch


if __name__ == '__main__':
    main()