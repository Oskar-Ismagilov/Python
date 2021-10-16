import time


class TrafficLight:
    colors = ["Red", "Yellow", "Green"]
    duration = [7, 2, 10]

    def __init__(self):
        self.__color = "Red"

    def running(self):
        for cycles in range(100):
            dur = 0
            for i in self.colors:
                self.__color = i
                print(self.__color)
                time.sleep(self.duration[dur])
                dur += 1


tl = TrafficLight()
tl.running()
