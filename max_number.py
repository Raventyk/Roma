#def max_number(a, b):
    #if a > b:
        #return a
    #else:
        #return b
#def max_number(a, b):
    #return {True: a, False: b}[a >= b]
def max_number(a, b):
    return (a + b + abs(a - b)) / 2  # математически , если без if и булевых подходов.


def test_max_number():
    assert max_number(1, 2) == 2
    assert max_number(17, 4) == 17
    assert max_number(-5, 6) == 6
    assert max_number(180, -4) == 180
    assert max_number(5,5) == 5
    assert max_number(-7,-7) == -7
    assert max_number(0,0) == 0
    print("Все тесты пройдены !")


test_max_number()

num1 = 17
num2 = 16

print(max_number(num1, num2))


def empty_function():
    pass


def even_numbers(n):
    for num in range(0, n + 1, 2):  # Без функции max  сделал используя функцию range
        yield num


for result in even_numbers(8):
    print(result)
