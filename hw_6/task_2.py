# Author: Victor Mamontov
# Make class Road

class Road:

    def __init__(self, length, width):
        self._length = length  # length of road in m
        self._width = width  # width of road in m

    def make_count(self, density, height):
        """:param density in kg
           :param height in cm
        """
        total_mass = self._length * self._width * density * height / 1000
        print(f'A total mass of asphalt: {total_mass} t')


new_road = Road(20, 5000)
new_road.make_count(25, 5)
