def numbers_input():
    number = input("Введите число от 1 до 5: ")

    try:
        int_number = int(number)
    except ValueError:
        print("Ошибка: вы ввели не число ")
        return None

    return int_number


def range_1_to_5(range):
    return 1 <= range <= 5


def eng_number_name(number):
    if number == 1:
        return "first"
    elif number == 2:
        return "second"
    elif number == 3:
        return "third"
    elif number == 4:
        return "fourth"
    elif number == 5:
        return "fifth"


def main():
    number = numbers_input()

    if number is None:
        return

    if range_1_to_5(number):
        print(eng_number_name(number))
    else:
        print("Число не входит в диапазон от 1 до 5")


main()
