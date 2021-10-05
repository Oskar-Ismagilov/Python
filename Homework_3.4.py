def my_func(x, y):
    elev = x
    for i in range(y, 1):
        elev = elev / x
    return elev


a = float(input("Введите число x: "))
b = int(input("Введите число y: "))
print(my_func(a, b))
print(a ** b)
