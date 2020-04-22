import random


def main():
    """
    Generates random addition problems for the user. Keeps track of
    the number of consecutive correct answers the user has achieved
    and keeps giving new problems until the user has solved 3 correct
    in a row.
    """
    consecutive_correct = 0

    # Continue asking questions until
    # the user gets 3 consecutively correct
    while consecutive_correct < 3:
        # Define random values to be added
        addend = random.randint(10, 99)
        augend = random.randint(10, 99)

        # Define the expected and user results
        expected = addend + augend
        total = ask_addition_question(addend, augend)

        # Check whether the results were consistent
        # and update the consecutive count
        # or reset it to zero.
        if total == expected:
            consecutive_correct += 1
            print("Correct! You've gotten " + str(consecutive_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer was " + str(expected) + ".")
            consecutive_correct = 0

    # When the user has completed 3 in a row,
    # give a congratulatory message!
    print("Congratulations! You mastered addition.")


def ask_addition_question(addend, augend):
    """
    Asks the user to add the values provided.
    :param addend: Number to be added to the augend.
    :param augend: Number to be added to the addend.
    :return: The sum of the added and augend.
    """
    total = int(input("What is " + str(addend) + " + " + str(augend) + " ? "))
    return total


if __name__ == "__main__":
    main()
