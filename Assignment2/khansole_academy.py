import random


def main():
    total_correct = 0

    while total_correct < 3:
        addend = random.randint(10, 99)
        augend = random.randint(10, 99)

        expected = addend + augend
        total = ask_addition_question(addend, augend)

        if total == expected:
            total_correct += 1
            print("Correct! You've gotten " + str(total_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer was " + str(expected) + ".")
            total_correct = 0

    print("Congratulations! You mastered addition.")


def ask_addition_question(addend, augend):
    total = int(input("What is " + str(addend) + " + " + str(augend) + " ? "))
    return total


if __name__ == "__main__":
    main()