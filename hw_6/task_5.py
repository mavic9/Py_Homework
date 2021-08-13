# Author: Victor Mamontov
# Make class Stationery with subclasses

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start for drawing {self.title}')


class Pen(Stationery):

    def draw(self):
        print(f'Start for drawing {self.title} with pen')


class Pencil(Stationery):

    def draw(self):
        print(f'Start for drawing {self.title} with pencil')


class Handle(Stationery):

    def draw(self):
        print(f'Start for drawing {self.title} with handle')


main_picture = Stationery('New project')
main_picture.draw()
picture_1 = Pen('New title')
picture_1.draw()
picture_2 = Pencil('New scheme')
picture_2.draw()
picture_3 = Handle('New object')
picture_3.draw()
