from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        repair_column()
        for i in range(4):
            move()
    repair_column()


def repair_column():
    turn_left()
    column_height = 0
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
        column_height += 1
    if no_beepers_present():
        put_beeper()
    turn_around()
    for i in range(column_height):
        move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
