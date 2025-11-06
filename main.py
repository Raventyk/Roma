print("# Сложение")
num1, num2 = input("Введите первое число "), input("Введите второе число ")
result = int(num1) + int(num2)
print("Результат сложения", result)
print("# Вычитание")
num1, num2 = input("Введите первое число "), input("Введите второе число ")
result = int(num1) - int(num2)
print("Результат вычитания", result)
print("# Умножения")
num1, num2 = input("Введите первое число "), input("Введите второе число ")
result = int(num1) * int(num2)
print("Результат умножения", result)
print("# Деление")
try:
    num1,num2 = input("Введите первое число "), input("Введите второе число ")
    result = int(num1) / int(num2)
except ZeroDivisionError:
    print("Деление на ноль не допустимо")
else:
    print(result)
finally:
    print("Завершение программы")
  
