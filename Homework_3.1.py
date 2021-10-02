def new_func():
    num1 = int(input("Введите число №1: "))
    num2 = int(input("Введите число №2: "))
    try:
        num1 / num2
    except ZeroDivisionError:
        return print("Ошибка: деление на 0")
    my_div = num1 / num2
    return my_div


print(new_func())

