from functools import reduce


def mult_nums(prev, curr):
    return prev * curr

my_list = [item for item in range(100, 1001, 2)]
print(reduce(mult_nums, my_list))


