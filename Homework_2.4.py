new_line = input("Введите слова через пробел: ")
new_list = new_line.split()
print(new_list)
c = len(new_list)
for i in range(0, c):
    print(new_list[i][0:10])
    c += 1
