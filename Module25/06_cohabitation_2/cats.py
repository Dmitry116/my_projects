class Cats:

    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety

    def eats(self):
        """Кот ест"""
        self.cat_eats = 20

    def sleeps(self):
        pass

    def runing_for_mouse(self):
        """Кот гоняется за мышью"""
        pass

    def bad_games(self):
        """Кот портит обои. грязи прибавляется 5"""
        pass

    def print_info_cat(self):
        """Выводится информация о кошке"""
        print('Кот\n'
              'Имя: {}\n'
              'Сытость: {}\n'.format(self.name, self.satiety))


class Cat_1(Cats):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety=30)


class Cat_2(Cats):
    def __init__(self, name, satiety=30):
        super().__init__(name, satiety=30)
