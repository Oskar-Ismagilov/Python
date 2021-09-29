my_list = [7, 5, 3, 3, 2]
numb = int(input("Введите число: "))
rev_list = []
mx = max(my_list)
mn = min(my_list)
if numb >= mx:
    my_list.insert(0, numb)
elif numb <= mn:
    my_list.insert(5, numb)
else:
    my_list.reverse()
    posit = my_list.index(numb)
    my_list.insert(posit, numb)
    my_list.reverse()
print(my_list)
