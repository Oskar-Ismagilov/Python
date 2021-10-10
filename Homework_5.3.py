with open('HW_5.3.txt') as file:
    content = file.readlines()
    full_dict = {}
    poor_employee = []
    numerator = 0
    denominator = 0
    for line in content:
        my_list = line.split()
        my_dict = {my_list[0]: my_list[1]}
        full_dict.update(my_dict)
    for key, value in full_dict.items():
        if float(value) < 20000:
            poor_employee.append(key)
        numerator += float(value)
        denominator += 1
    print(f'Список сотрудников с окладом менее 20000 руб.: {poor_employee}')
    if denominator == 0:
        print("Деление на 0")
    else:
        print(f'Средний оклад сотрудников составляет {round(numerator/denominator, 2)} руб.')
