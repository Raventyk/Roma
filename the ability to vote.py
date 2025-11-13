def can_vote(age, citezen, out_human):
    if age < 18:
        return False
    if citezen == "нет":
        return False
    if out_human == "да":
        return False
    return True


def data():
    age = int(input("Введите Ваш возраст "))
    citezen = input("Вы гражданин страны ? (Введите 'Да' или 'Нет') ").lower()
    out_human = input("Есть ли у вас судимость или запрет на голосование? (Введите 'Да' или 'Нет') ").lower()
    return age, citezen, out_human


def main():
    age, citezen, out_human = data()

    if can_vote(age, citezen, out_human):
        print("Голосуйте!")
    else:
        print("Вам нельзя голосовать!")

main()
