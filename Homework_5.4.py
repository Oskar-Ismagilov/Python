with open('HW_5.4.txt', 'r+') as file:
    content = file.readlines()
    russ_list = ['Один', 'Два', 'Три', 'Четыре']
    full_list = []
    join_list = []
    num = 0
    for line in content:
        new_content = line.split()
        new_content.pop(0)
        new_content.insert(0, russ_list[num])
        full_list.append(new_content)
        num += 1
with open('HW_5.4.1.txt', 'w') as new_file:
    for item in full_list:
        join_list = " ".join(item)
        new_file.writelines(f'{join_list}\n')



