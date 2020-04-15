from karel.stanfordkarel import *

from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    # If our world has a width of 1, turn left to checker upward
    if front_is_blocked():
        turn_left()

    # While we have an available path, checker right, turn, then
    # checker back to the left, and repeat.
    while front_is_clear():
        # Move to the right first and turn around at the end
        # Even-numbered size
        if checker_straight():
            new_row_right()
        # Odd-numbered size
        else:
            put_beeper()
            new_row_right()
            if front_is_clear():
                move()

        # Move to the left and turn around at the end
        # after checking if we're already at the end of the world
        if front_is_clear():
            if checker_straight():
                new_row_left()
            else:
                put_beeper()
                new_row_left()
                if front_is_clear():
                    move()


def checker_straight():
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
        else:
            return True
    return False


def new_row_right():
    turn_left()
    if front_is_clear():
        move()
        turn_left()


def new_row_left():
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def checker_up():
    num = 0
    while front_is_clear():
        move()
        put_beeper()
        num += 1
        if front_is_clear():
            move()
            num += 1
    turn_right()
    if num % 2 == 0:
        return True
    return False


def checker_down(even):
    if even:
        put_beeper()
        move()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
