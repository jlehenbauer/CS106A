def convert_to_dog_years(human_years):
    dog_years = human_years * 7
    return dog_years


def main():
    human_age = float(input('Enter human age: '))
    dog_age = convert_to_dog_years(human_age)
    print('Dog age is:', dog_age)


if __name__ == '__main__':
    main()