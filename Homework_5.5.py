from random import random


with open('HW_5.5.txt', 'w+') as file:
    sum_num = 0
    for item in range(10):
        file.writelines(f'{int((round(10 * random(),0)))} ')
    file.seek(0)
    content = file.readlines()
    print(content)
    for item in content:
        new_content = item.split()
    for num in new_content:
        sum_num += int(num)
    print(f'Сумма чисел = {sum_num}')
    
