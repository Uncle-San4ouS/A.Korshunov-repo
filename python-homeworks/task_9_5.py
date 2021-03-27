class Stationary:
    def __init__(self, title='Чем бы порисовать...'):
        self.title = title

    def draw(self):
        print(f'Давайте порисуем! {self.title}')

class Pen(Stationary):
    def draw(self):
        print(f'Начнём-с! {self.title} О, есть ручка, даже пишет!')

class Pencil(Stationary):
    def draw(self):
        print(f'Начнём-с! {self.title} Ой, карандашик, даже наточен!')

class Handle(Stationary):
    def draw(self):
        print(f'Начнём-с! {self.title} Ого! Маркер! Хоть на заборе, хоть на стенах рисуй!')

stat = Stationary()
stat.draw()
pen = Pen("BIC")
pen.draw()
pencil = Pencil("ДЕЛОВОЙ")
pencil.draw()
marker = Handle("MARK")
marker.draw()