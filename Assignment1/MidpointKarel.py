from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel moves across the room and records how many
    spaces they move. To do this, Karel places beepers
    at either end of the room, then rebounds between
    them, placing new beepers as Karel finds spaces
    without them. When Karel encounters a repeat beeper
    for the first time, the midpoint has been found!
    Clear all unnecessary beepers and return to the middle.
    """
    place_beepers_at_endpoints()

    # Rebound between endpoints, placing beepers until
    # ending on one. This is the midpoint!
    while no_beepers_present():
        move_until_beeper()
        turn_around()
        if front_is_clear():
            move()
        if no_beepers_present():
            put_beeper()
            if front_is_clear():
                move()

    # Remove unnecessary beepers in one direction
    clear_beepers_in_row()

    # Clear in the other direction, if possible
    if front_is_clear():
        move()
        clear_beepers_in_row()

    # Move onto the remaining beeper (midpoint)
    if front_is_clear():
        move_until_beeper()


def place_beepers_at_endpoints():
    """
    pre-condition: Karel starts at 1, 1 (bottom-left)

    post-condition: Karel is facing west and has moved off the beeper, if possible
    """
    for i in range(2):
        move_until_wall()
        turn_around()
        if no_beepers_present():
            put_beeper()
            if front_is_clear():
                move()


def clear_beepers_in_row():
    """
    pre-condition: Karel is on the space past the midpoint facing toward a wall

    post-condition: Karel is facing the midpoint
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        turn_around()
        if front_is_clear():
            pick_beeper()


def move_until_wall():
    while front_is_clear():
        move()


def move_until_beeper():
    while no_beepers_present():
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
