class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asphalt_mass(self, mass, thickness):
        self.mass = mass
        self.thickness = thickness
        print(f"Масса асфальта составляет: {self._width * self._length * self.mass * self.thickness / 1000} т")

my_road = Road(5000, 20)
my_road.asphalt_mass(25, 5)
