class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def result(self, weight=25, thickness=5):
        return f'{self._lenght} м * {self._width} м * {weight} кг *{thickness} см =' \
               f' {(self._lenght * self._width * weight * thickness) / 1000} т'

road = Road(5000, 20)
print(road.result())