choice_mood = {
    0: 'Плохое настроение!',
    1: 'Веселое настроение!'
}

choice_hunger = {
    0: 'Голоден',
    1: 'Сытый'
}


class Children:

    def __init__(self, name_child, year_child):
        self.name_child = name_child
        self.year_child = year_child

    """Настроение ребенка"""

    def mood_child(self, num):
        self.mood = choice_mood[num]

    """Голод ребенка"""

    def hunger_child(self, num):
        self.hunger = choice_hunger[num]

    def print_info(self):
        print('Имя: {}\n'
              'Возраст: {}\n'
              'Состояние: {}\n'
              'Сытость: {}'.format(self.name_child, self.year_child, self.mood, self.hunger))
