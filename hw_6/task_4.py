# Author: Victor Mamontov
# Make class Cas with subclasses

class Car:

    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} goes')

    def stop(self):
        print(f'Car {self.name} stops')

    def turn(self, direction):
        print(f'Car {self.name} turns {direction}')

    def show_speed(self):
        print(f'{self.name}\'s speed is {self.speed} km/h')

    def which_car(self):
        if self.is_police:
            print(f'{self.name} is a police car!')
        else:
            print(f'{self.name} is not a police car!')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}\'s speed is {self.speed} km/h. Reduce your speed!')
        else:
            print(f'{self.name}\'s speed is {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}\'s speed is {self.speed} km/h. Reduce your speed!')
        else:
            print(f'{self.name}\'s speed is {self.speed} km/h')


class PoliceCar(Car):
    pass


car_1 = TownCar(70, 'Reno', 'grey', False)
car_1.which_car()
car_1.show_speed()
car_1.go()
car_1.turn('left')

car_2 = PoliceCar(80, 'Volkswagen', 'grey', True)
car_2.which_car()
car_2.show_speed()
car_2.go()
car_2.turn('right')

car_3 = WorkCar(10, 'Isuzu', 'grey', False)
car_3.which_car()
car_3.show_speed()
car_3.stop()
