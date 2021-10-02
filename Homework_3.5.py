def my_func():
    a = 0
    key = 0
    my_str = input("Введите через пробел числа (для завершения нажмите *): ")
    my_list = my_str.split(" ")
    for i in range(len(my_list)):
        if my_list[i] == "*":
            key = 1
            break
        else:
            a += float(my_list[i])
    return a, key


func_stage = 0
my_sum = 0
k = 0
while k == 0:
    func_stage, k = my_func()
    if func_stage is None:
        break
    else:
        my_sum += func_stage
        print(my_sum)

