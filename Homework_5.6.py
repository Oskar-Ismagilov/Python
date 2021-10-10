with open('HW_5.6.txt', 'r') as file:
    content = file.readlines()
    academ_subj = []
    hour_list = []
    sum_num = 0
    my_dict = {}
    count_subj = 0
    for item in content:
        new_item = item.split(":")
        academ_subj.append(new_item[0])
        for char in new_item[1]:
            if ord(char) >= 48 and ord(char) <= 57:
                hour_list.append(f'{char}')
            else:
                hour_list.append(' ')
        num_list = ''.join(hour_list).split()
        for i in num_list:
            sum_num += int(i)
        key = academ_subj[count_subj]
        my_dict.update({key: sum_num})
        count_subj += 1
        hour_list = []
        sum_num = 0
    print(my_dict)
