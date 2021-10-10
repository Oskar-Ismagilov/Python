with open("HW_5.1.txt", 'w') as file:
    k = 0
    lines = []
    while k < 100:
        curr_line = input("Введите строки: ")
        if not curr_line:
            break
        lines.append(f'{curr_line}\n')
        k += 1
    file.writelines(lines)
