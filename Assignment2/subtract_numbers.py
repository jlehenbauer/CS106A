
def main():
    """
    This will ask the user for two numbers
    and subtract the second number from the
    first number.
    :return: double
    """
    print("This program subtracts one number from another.")

    # Define variables to be subtracted
    minuend = float(input("Enter first number: "))
    subtrahend = float(input("Enter second number: "))

    difference = minuend - subtrahend

    print("The result is " + str(difference))

    return difference


if __name__ == "__main__":
    main()
