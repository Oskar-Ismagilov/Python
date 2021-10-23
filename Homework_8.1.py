class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_nums(cls, date):
        cls.date = date
        num_list = date.split('-')
        return num_list

    @staticmethod
    def date_valid(day, month, year):
        my_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
        if (int(day) <= my_dict[str(month)]) and (1 <= int(month) <= 12) and (int(year) in range(0, 2100)):
            return f'Формат даты корректный'
        else:
            return f'Формат даты некорректный'


date_in_nums = Date.date_to_nums("31-02-2021")
print(date_in_nums)
day_1 = int(date_in_nums[0])
month_1 = int(date_in_nums[1])
year_1 = int(date_in_nums[2])
print(Date.date_valid(day_1, month_1, year_1))
