class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_income(self):
        return f'{sum(self._income.values())}'

tester = Position('Aleksandr', 'Korshunov', 'QA', 80000, 40000)
print(tester.get_full_name())
print(tester.position)
print(tester.get_full_income())