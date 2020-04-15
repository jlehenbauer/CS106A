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
    even = False
    turn_left()
    while front_is_clear():
        if checker_up():
            even = True
        if front_is_clear():
            move()
            turn_right()
            checker_down(even)
        if front_is_clear():
            move()
            turn_left()


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


if __name__ == "__main__":
    run_karel_program()
