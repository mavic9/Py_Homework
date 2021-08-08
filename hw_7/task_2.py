# Author: Victor Mamontov
# Make class Clothes with abstract method

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def count_fabric(self):
        pass


class Suit(Clothes, ABC):

    def __init__(self, height):
        self.height = height

    @property
    def count_fabric(self):
        fabric = 2 * self.height + 0.3
        return round(fabric, 2)


class Coat(Clothes, ABC):

    def __init__(self, size):
        self.size = size

    @property
    def count_fabric(self):
        fabric = self.size / 6.5 + 0.5
        return round(fabric, 2)


my_coat = Coat(50)
print(my_coat.count_fabric)
my_suit = Suit(1.8)
print(my_suit.count_fabric)
