name = []
price = []
number = []
ed = []
final_list = []
my_dict = {}
new_dict = {}
my_list = []
for i in range(3):
    name.append(input(f"Введите название товара № {i + 1}: "))
print(name)
for i in range(3):
    price.append(int(input(f"Введите цену товара № {i + 1}: ")))
print(price)
for i in range(3):
    number.append(int(input(f"Введите количество товаров № {i + 1}: ")))
print(number)
for i in range(3):
    ed.append(input(f"Введите единицу измерения для товара № {i + 1}: "))
print(ed)
for j in range(3):
    my_dict.update({'название': name[j],
                    'цена': price[j],
                    'количество': number[j],
                    'ед': ed[j]
                    })
    my_list.append(j + 1)
    my_list.append(my_dict.copy())
first_product = tuple(my_list[0:2])
second_product = tuple(my_list[2:4])
third_product = tuple(my_list[4:6])
final_list.append(first_product)
final_list.append(second_product)
final_list.append(third_product)
print(final_list)
new_dict.update({"название": name,
                 "цена": price,
                 "количество": number,
                 "ед": ed
                 })
print(new_dict)
