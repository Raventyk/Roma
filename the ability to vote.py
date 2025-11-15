#def can_vote(age, citezen, out_human):
    #if age < 18:
        #return False
    #if citezen == "нет":
        #return False
    #if out_human == "да":
        #return False
    #return True
def can_vote(age, citezen, out_human):
    if age < 18 or citezen == "нет" or out_human == "да":
        return False
        #return False
    #if citezen == "нет":
        #return False
    #if out_human == "да":
        #return False
    return True

def input_data():
    input_age = input("Введите Ваш возраст ")

    try:
        age = int(input_age)
    except ValueError:
        print("Ошибка : Вы ввели не числовое значение ")
        age = 0

    citezen = input("Вы гражданин страны ? (Введите 'Да' или 'Нет') ").lower().strip()
    out_human = input("Есть ли у вас судимость или запрет на голосование? (Введите 'Да' или 'Нет') ").lower().strip()
    return age, citezen, out_human


def main():
    age, citezen, out_human = input_data()

    if can_vote(age, citezen, out_human):
        print("Голосуйте!")
    else:
        print("Вам нельзя голосовать!")


main()
