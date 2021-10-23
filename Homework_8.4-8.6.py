class Warehouse:
    def __init__(self, equipments=None):
        if not equipments:
            equipments = []
        self.equipments = equipments

    def add_equipment(self, equipment, department):
        if department.return_equipment(equipment):
            self.equipments.append(equipment)
        else:
            print('Данного оборудования нет в указанном департаменте!')

    def get_equipment(self, equipment, department):
        if equipment in self.equipments:
            self.equipments.remove(equipment)
            department.add_equipment(equipment)
        else:
            print("Такого оборудования нет на складе")


class OfficeEquipment:
    def __init__(self, model):
        self.model = model

    def __repr__(self):
        return f'{self.model}'


class Printer(OfficeEquipment):
    def __init__(self, model):
        super(Printer, self).__init__(model)
        self.type = 'Printer'


class Scanner(OfficeEquipment):
    def __init__(self, model):
        super(Scanner, self).__init__(model)
        self.type = 'Scanner'


class Copier(OfficeEquipment):
    def __init__(self, model):
        super(Copier, self).__init__(model)
        self.type = 'Copier'


class Department:
    def __init__(self, name, equipments=None):
        if not equipments:
            equipments = []
        self.equipments = equipments
        self.name = name

    def add_equipment(self, equipment):
        self.equipments.append(equipment)

    def return_equipment(self, equipment):
        if equipment in self.equipments:
            self.equipments.remove(equipment)
            return True
        else:
            return False


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


equipment_1 = Printer("HP LaserJet 1200")
equipment_2 = Printer("HP LaserJet 1856")
equipment_3 = Scanner("HP ScanJet G2410")
equipment_4 = Scanner("HP ScanJet G6823")
equipment_5 = Copier("HP LaserJet M1132")
equipment_6 = Copier("HP LaserJet M5489")

warehouse_1 = Warehouse([equipment_2, equipment_3, equipment_4])

depart_1 = Department("Infrastructure", [equipment_1])
depart_2 = Department("Commercial", [equipment_5])
depart_3 = Department("PR", [equipment_6])

warehouse_1.get_equipment(equipment_2, depart_1)
print(warehouse_1.equipments)
print(depart_1.equipments)
warehouse_1.add_equipment(equipment_5, depart_2)

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num_return_equip = input("Введите количество принтеров, отправленных на склад: ")
for item in num_return_equip:
    try:
        if item not in num_list:
            raise MyException("Введено не число!")
    except MyException as err:
        print(err)
