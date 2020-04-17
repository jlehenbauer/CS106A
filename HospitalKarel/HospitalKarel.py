from karel.stanfordkarel import *


def main():
    # while front_is_clear(): Move until Karel reaches a beeper
    # if beeper_present(): Build a hospital there!
    # while front_is_clear(): Move until Karel reaches a beeper

    while front_is_clear():
        move()
        if beepers_present():
            build_a_hospital()


def build_a_hospital():
    """
    pre-condition: We are on a space where a
        hospital needs to be built, and we
        are standing on one beeper

    post-condition: We are on the bottom-right
        corner of a hospital facing west
    """
    pick_beeper()
    turn_left()
    build_a_wall()
    turn_right()
    move()
    turn_right()
    build_a_wall()
    turn_left()


def build_a_wall():
    """
    TODO: write pre- and post-conditions
    """
    for i in range(2):
        put_beeper()
        move()
    put_beeper()


def turn_right():
    """
    TODO: write pre- and post-conditions
    """
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
