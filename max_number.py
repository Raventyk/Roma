def max_number(a, b):
    return (a + b + abs(a - b)) / 2  # математически , если без if и булевых подходов.


def test_max_number():
    assert max_number(32, -522) == 32
    assert max_number(-180, 44) == 44
    assert max_number(5,5) == 5
    print("Все тесты пройдены !")


def empty_function():
    pass


def even_numbers(n):
    for num in range(0, n + 1, 2):  # Без функции max  сделал используя функцию range
        yield num


test_max_number()

for result in even_numbers(8):
    print(result)

num1 = 17
num2 = 16
print(max_number(num1, num2))
