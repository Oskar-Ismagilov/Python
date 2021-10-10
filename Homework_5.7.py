import json


with open('HW_5.7.txt', 'r') as file:
    profit_list = []
    avg_prof_dict = {}
    full_list = []
    firm_count = 0
    sum_prof = 0
    firm_dict = {}
    content = file.readlines()
    for item in content:
        my_list = item.split()
        profit = float(my_list[2]) - float(my_list[3])
        if profit > 0:
            print(f'Прибыль компании {my_list[0]} составила {profit} руб.')
        else:
            print(f'Компания {my_list[0]} не прибыльная')
        profit_list.append(profit)
        firm_dict.update({my_list[0]: profit})
    for item in profit_list:
        if item > 0:
            sum_prof += float(item)
            firm_count += 1
    avg_prof = sum_prof / firm_count
    print(profit_list)
    print(f'Средняя прибыль компаний составила {avg_prof} руб.')
    avg_prof_dict.update({"Average profit": avg_prof})
    print(firm_dict)
    print(avg_prof_dict)
    full_list.append(firm_dict)
    full_list.append(avg_prof_dict)
    print(full_list)
with open('HW_5.7.json', 'w') as json_file:
    json.dump(full_list, json_file)
