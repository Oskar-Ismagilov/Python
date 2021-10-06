def fact(n):
    for i in range(1, n + 1):
       yield i


mult_nums = 1
n = int(input("Введите число n: "))
for el in fact(n):
    mult_nums = mult_nums * el
    print(mult_nums)
