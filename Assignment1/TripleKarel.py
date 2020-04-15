from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel repeats painting 3 walls on 3 buildings, turning right
    when she reaches a new building.
    """
    for building in range(3):
        for wall in range(3):
            paint_wall()
            if wall < 2:
                turn_left()
                move()
        turn_right()


def paint_wall():
    """
    Karel paints as long as she has a wall to her left.
    """
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
