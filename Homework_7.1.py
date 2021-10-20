class Matrix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        my_str_list = []
        my_str = ""
        for item in range(len(self.value)):
            my_str += f"{self.value[item]}\n"
            # my_str_list.append(my_str)
            # print(str(my_str_list))
        return my_str

    def __add__(self, other):
        sum_num_list = []
        sum_str_list = []
        new_str = []
        for item in range(len(self.value)):
            my_str = self.value[item]
            other_str = other.value[item]
            for number in range(len(my_str)):
                sum_num_list.append(my_str[number] + other_str[number])
            sum_str_list.append(sum_num_list)
            sum_num_list = []
        value = sum_str_list
        return Matrix(value)


my_list_1 = [[2, 5, 8], [3, 8, 5], [9, 4, 7]]
my_list_2 = [[6, 3, 2], [9, 0, 6], [1, 2, 3]]
my_matrix_1 = Matrix(my_list_1)
my_matrix_2 = Matrix(my_list_2)
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_1 + my_matrix_2)

