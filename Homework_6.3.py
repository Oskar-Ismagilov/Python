class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        sum_income = self._income["wage"] * 12 + self._income["bonus"]
        print(f"Общий доход сотрудника составил: {sum_income} руб.")


worker_1 = Position("Ivan", "Petrov", "Manager", 500, 5000)
worker_1.get_full_name()
worker_1.get_total_income()

worker_2 = Position("Petr", "Sidorov", "Expert", 450, 3000)
worker_2.get_full_name()
worker_2.get_total_income()