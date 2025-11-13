def can_vote(age, citezen, out_human):
    try:
        age = int(age)
    except ValueError:
        print("Вы ввели не числовые значения ")
        return False

    if age < 18:
        return False
    if citezen == "нет":
        return False
    if out_human == "да":
        return False
    return True


def data():
    age = (input("Введите Ваш возраст "))
    citezen = input("Вы гражданин страны ? (Введите 'Да' или 'Нет') ").lower().strip()
    out_human = input("Есть ли у вас судимость или запрет на голосование? (Введите 'Да' или 'Нет') ").lower().strip()
    return age, citezen, out_human


def main():
    age, citezen, out_human = data()

    if can_vote(age, citezen, out_human):
        print("Голосуйте!")
    else:
        print("Вам нельзя голосовать!")

main()
