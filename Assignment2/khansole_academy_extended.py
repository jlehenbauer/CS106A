import random

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4


def main():
    """
    Generates a random problem for the user.
    User can choose between the four basic operations
    and will keep getting questions until they answer
    3 in a row correctly.
    """
    consecutive_correct = 0

    # Ask the user which operation they would like to practice.
    print_options()
    operation = ""
    while not operation.isdigit():
        operation = input("Choose a number: ")
    operation = int(operation)

    # Continue asking questions until
    # the user gets 3 consecutively correct
    while consecutive_correct < 3:
        # Define random values to be used
        first_number = random.randint(10, 99)
        second_number = random.randint(10, 99)
        expected = None
        user_answer = None

        # Define the expected and user results
        if operation == ADDITION:
            expected = first_number + second_number
            user_answer = ask_addition_question(first_number, second_number)
        elif operation == SUBTRACTION:
            expected = first_number - second_number
            user_answer = ask_subtraction_question(first_number, second_number)
        elif operation == MULTIPLICATION:
            expected = first_number * second_number
            user_answer = ask_multiplication_question(first_number, second_number)
        elif operation == DIVISION:
            expected = first_number / second_number
            user_answer = ask_division_question(first_number, second_number)

        # Check whether the results were consistent
        # and update the consecutive count
        # or reset it to zero.
        if user_answer == expected:
            consecutive_correct += 1
            print("Correct! You've gotten " + str(consecutive_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer was " + str(expected) + ".")
            consecutive_correct = 0

    # When the user has completed 3 in a row,
    # give a congratulatory message!
    print("Congratulations! You mastered another operation.")


def ask_addition_question(addend, augend):
    """
    Asks the user to add the values provided.
    :param addend: Number to be added to the augend.
    :param augend: Number to be added to the addend.
    :return: The sum of the added and augend.
    """
    total = int(input("What is " + str(addend) + " + " + str(augend) + "? "))
    return total


def ask_subtraction_question(subtrahend, minuend):
    """
    Asks the user to add the values provided.
    :param subtrahend: Number to be subtracted from.
    :param minuend: Number to be subtracted from the subtrahend.
    :return: The difference of the subtrahend and minuend.
    """
    difference = int(input("What is " + str(subtrahend) + " - " + str(minuend) + "? "))
    return difference


def ask_multiplication_question(multiplicand, multiplier):
    """
    Asks the user to add the values provided.
    :param multiplicand: Number to be multiplied by the multiplier.
    :param multiplier: Number to be multiplied by the multiplicand.
    :return: The product of the multiplicand and multiplier.
    """
    product = int(input("What is " + str(multiplicand) + " x " + str(multiplier) + "? "))
    return product


def ask_division_question(dividend, divisor):
    """
    Asks the user to add the values provided.
    :param dividend: Number to be divided by the divisor.
    :param divisor: Number to divide the dividend.
    :return: The quotient of the dividend and divisor.
    """
    quotient = int(input("What is " + str(dividend) + " / " + str(divisor) + "? "))
    return quotient


def print_options():
    print("What operation would you like to practice?")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")


if __name__ == "__main__":
    main()
