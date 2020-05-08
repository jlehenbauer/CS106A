"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage

BLUE_THRESHOLD = 1.5

def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')

    for px in foreground:
        average = (px.red + px.blue + px.green) // 3
        if px.blue < average * BLUE_THRESHOLD:
            background.set_pixel(px.x, px.y, px)

    background.show()


if __name__ == '__main__':
    main()