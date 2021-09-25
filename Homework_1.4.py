a = int(input("Введите целое положительное письмо: "))
c = 1
while a > 0:
    b = a % 10
    if b > c:
        c = b
    a = a // 10
print(c)
