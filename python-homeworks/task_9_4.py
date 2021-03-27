class Car:
    '''Автомобиль'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Автомобиль в студию! {self.name} (цвет кузова: {self.color}), принадлежность к МВД: {self.is_police}')

    def go(self):
        print(f'{self.name} поехал!')

    def stop(self):
        print(f'{self.name} остановился.')

    def turn(self, direction):
        print(f'{self.name} повернул {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км/ч.'

class TownCar(Car):
    '''Chevrolet Aveo'''
    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км/ч - превышает, гад!' \
            if self.speed > 60 else f'{self.name} движется со скоростью {self.speed} км/ч.'

class WorkCar(Car):
    '''ЗиЛ-121'''
    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км/ч - превышает, гад!' \
            if self.speed > 40 else f'{self.name} движется со скоростью {self.speed} км/ч.'

class SportCar(Car):
    '''Bugatti Veyron'''

class PoliceCar(Car):
    '''Mitsubishi Lancer X'''
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

town_car = TownCar('Марианна Анатольевна', 'белый', 50)
town_car.go()
print(town_car.show_speed())
town_car.turn(1)
town_car.stop()
print()

work_car = WorkCar('"Мусоровоз"', 'оранжевый', 38)
work_car.go()
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

sport_car = SportCar('Вася-лихач', 'metalic INDIGO', 200)
sport_car.go()
print(sport_car.show_speed())
sport_car.turn(1)
sport_car.turn(0)
sport_car.turn(1)
sport_car.stop()
print()

police_car = PoliceCar('"ДПС"', '"Динамо"', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.turn(0)
police_car.turn(0)
police_car.stop()
print()

print(f'\nНарушитель {sport_car.name} на автомобиле цвета {sport_car.color} скрылся во дворах от автомобиля {police_car.name}.')