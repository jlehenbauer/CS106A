"""
Write a program to prompt the user for a weight on earth and print
the equivalent weight on the moon.
"""

def main():
    # Take earth weight from the user
    earth_weight = float(input("Enter weight on earth: "))

    # Convert to moon weight by multiplying by 0.165
    moon_weight = 0.165 * earth_weight

    # Give back to user
    print("The weight on the moon would be " + str(moon_weight))


if __name__ == '__main__':
    main()
