initial_list = []
target_list = []
a = 0
b = int(input("Введите длину списка: "))
for i in range(0, b):
    initial_list.append(input(f"Введите число N{i + 1}: "))
print(initial_list)
if b % 2 == 0:
    for i in range(b // 2):
        target_list.append(initial_list[a + 1])
        target_list.append(initial_list[a])
        a += 2
else:
    for i in range((b - 1) // 2):
        target_list.append(initial_list[a + 1])
        target_list.append(initial_list[a])
        a += 2
    target_list.append(initial_list[-1])
print(target_list)
