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
    spaces she moves. She then turns around, travels
    halfway (rounding down) back, and places a beeper.
    """
    while no_beepers_present():
        move_until_object()
        turn_around()
        if front_is_clear():
            move()
        if no_beepers_present():
            put_beeper()
        else:
            return
        if front_is_clear():
            move()

    clear_beepers_in_row()

    turn_around()

    move_until_object()

    if front_is_clear():
        move()

    clear_beepers_in_row()

    turn_around()

    move_until_object()


def clear_beepers_in_row():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()


def move_until_object():
    while front_is_clear() and no_beepers_present():
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
