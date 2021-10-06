from itertools import count, cycle


my_list = ["one", 'two', "three", "four", "five"]
for i in count(3):
    print(i)
    if i > 9:
        break
num = 0
for j in cycle(my_list):
    print(j)
    num += 1
    if num > 5:
        break

