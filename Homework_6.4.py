class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина повернула {self.direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля составляет {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")

class WorkCar(Car):
     def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


t_car = TownCar(70, "white", "VW Polo")
print(f"Автомобиль {t_car.name}")
t_car.go()
t_car.turn("вправо")
t_car.show_speed()
t_car.stop()

w_car = WorkCar(35, "black", "Toyota Hilux")
print(f"\nАвтомобиль {w_car.name}")
w_car.go()
w_car.turn("влево")
w_car.show_speed()
w_car.stop()

s_car = SportCar(250, "red", "Ferrari F350")
print(f"\nАвтомобиль {s_car.name}")
s_car.go()
s_car.turn("вправо")
s_car.show_speed()

p_car = PoliceCar(80, "police", "Ford Focus")
print(f"\nАвтомобиль {p_car.name}")
p_car.go()
p_car.turn("влево")
p_car.show_speed()
if p_car.is_police:
    print("Полицейский автомобиль")
