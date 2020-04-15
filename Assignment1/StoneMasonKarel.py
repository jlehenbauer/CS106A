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
    Karel moves forward, repairing columns every four spaces.
    """
    while front_is_clear():
        repair_column()
        for i in range(4):
            move()
    repair_column()


def repair_column():
    """
    The repair_column() method directs Karel upward, places
    beepers anywhere they're missing, then returns to the
    floor and repositions herself to face east.
    """
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
