import random

# Define constant for number of random numbers to print
NUM_RANDOM = 10


def main():
    """
    Prints NUM_RANDOM random numbers between 1 and 100.
    """
    for i in range(NUM_RANDOM):
        print(random.randint(1, 100))


if __name__ == "__main__":
    main()
