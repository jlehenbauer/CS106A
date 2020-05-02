def main():
    total = 0
    user_num = int(input("Enter a value: "))
    while user_num != 0:
        total += user_num
        print("Running total is " + str(total))
        user_num = int(input("Enter a value: "))


if __name__ == '__main__':
    main()