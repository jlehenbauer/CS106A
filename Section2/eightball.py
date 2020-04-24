"""
Write a program to simulate a magic eight ball. The program should
let the user type a yes or no question and pick a random answer from a
set of 6 predetermined answers.
"""
import random
MAX_RESPONSES = 6


def main():
    user_question = None

    while user_question != "":
        user_question = input("Ask a yes or no question: ")

        response = random.randint(1, MAX_RESPONSES)
        response1 = "As I see it..."
        response2 = "Ask again later"
        response3 = "Better not tell you now."
        response4 = "Cannot predict now."
        response5 = "Concentrate and ask again"
        response6 = "Yes!"

        if response == 1:
            print(response1)
        if response == 2:
            print(response2)
        if response == 3:
            print(response3)
        if response == 4:
            print(response4)
        if response == 5:
            print(response5)
        if response == 6:
            print(response6)


if __name__ == '__main__':
    main()
