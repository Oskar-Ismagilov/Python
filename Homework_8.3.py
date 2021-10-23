class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


target_list = []
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
switch = 0
while switch == 0:
    data = input("Введите данные (для остановки введите stop): ")
    if data == "stop":
        print(target_list)
        switch = 1
    else:
        for item in data:
            try:
                if item in num_list:
                    target_list.append(item)
                else:
                    raise MyException("Введено не число!")
            except MyException as err:
                print(err)
