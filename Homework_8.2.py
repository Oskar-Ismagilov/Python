class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


numerator = float(input("Введите числитель: "))
denominator = float(input("Введите знаменатель: "))

try:
    if denominator == 0:
        raise MyException("Деление на ноль!")
    else:
        num = numerator/denominator
        print(num)
except MyException as err:
    print(err)
