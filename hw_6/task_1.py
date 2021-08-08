# Author: Victor Mamontov
# Make class TrafficLight

class TrafficLight:

    __color = ('Red', 'Yellow', 'Green')

    def running(self):
        import time
        if TrafficLight.__color[0] == 'Red' and TrafficLight.__color[1] == 'Yellow' and TrafficLight.__color[2] == 'Green':
            k = 0
            while k < 10:
                print(TrafficLight.__color[0])
                time.sleep(7.0)
                print(TrafficLight.__color[1])
                time.sleep(2.0)
                print(TrafficLight.__color[2])
                time.sleep(10.0)
                k += 1
        else:
            print('Traffic light is not functional!')


new_traffic = TrafficLight()
new_traffic.running()
