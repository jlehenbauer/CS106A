from karel.stanfordkarel import *


def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()  # need to be facing east


def build_hospital():
    """
    precondition: on a pile of supplies (a beeper)
    postcondition: facing east
    """
    pick_beeper()
    turn_left()
    place_three_beepers()
    turn_right()
    move()
    turn_right()
    place_three_beepers()
    turn_left()


def place_three_beepers():
    """
    Pre: Karel is facing the direction of the column, at the base of the column
    Post: Karel is at the end of a 3-beeper column, facing away from the base
    """
    for i in range(2):
        put_beeper()
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
