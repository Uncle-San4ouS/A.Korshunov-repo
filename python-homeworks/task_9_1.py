import time
import itertools

class TrafficLight:
    __color = [['STOP',[7, 31]], ['wait', [2, 33]], ['GO!', [5, 32]], ['wait', [2, 33]]]

    def running(self):
        for color in itertools.cycle(self.__color):
            print(f'\r\033[{color[1][1]}m\033[1m{color[0]}\033[0m', end='')
            time.sleep(color[1][0])

t_l = TrafficLight()
t_l.running()