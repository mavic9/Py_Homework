# Author: Victor Mamontov
# Make class Road

class Road:

    def __init__(self, length, width):
        self._length = length  # length of road in m
        self._width = width  # width of road in m

    def make_count(self):
        density = 2.5  # density of asphalt in tons per 1 cubic m
        height = 0.05  # height of asphalt in m
        total_mass = self._length * self._width * density * height
        print(f'A total mass of asphalt: {total_mass} t')


new_road = Road(20, 5000)
new_road.make_count()
