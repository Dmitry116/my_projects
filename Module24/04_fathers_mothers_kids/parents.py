choice_mood = {
    0: 'Плохое настроение!',
    1: 'Веселое настроение!'
}

choice_hunger = {
    0: 'Голоден',
    1: 'Сытый'
}


class Parent:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.children = {}

    def print_info(self):
        print('Имя: {}\n'
              'Возраст: {}'.format(self.name, self.year))
        for name, year in self.children.items():
            print(f'Ребенку {name} {year} лет')
        print()

    def add_child(self, name, year):
        self.children[name] = year

    """Игра с ребенком"""

    def play_with_child(self, child):
        print(f'Папа поиграл с {child}')
        print(f'Настроение {child}: {choice_mood[1].lower()}')

    """Кормление ребенка"""

    def feed_child(self, child):
        print(f'{child} поел и теперь он {choice_hunger[1].lower()})')
