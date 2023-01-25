class Cats:
    """В __init__ параметры имя, apartment ссылка на класс Home,
    сытость по умолчанию 30"""
    def __init__(self, name, apartment, satiety=30):
        self.name = name
        self.apartment = apartment
        self.cat_satiety = satiety

    def check_cat_satiety(self):
        """Проверка на сытость кота"""
        if self.cat_satiety <= 0:
            print(f'{self.name} умер от голода...\n'
                  f'Конец игры!')

    def cat_eating(self):
        """Кот ест. сытость увеличивается на 20. запас еды уменьшается на 10"""
        if self.apartment.FOOD_CATS < 10:
            print('У кошек закончилась еда')
        else:
            self.cat_satiety += 20
            self.apartment.FOOD_CATS -= 10

    def sleeps(self):
        print(f'Кот {self.name} спит!')

    def runing_for_mouse(self):
        """Кот гоняется за мышью, грязь в доме увеличивается на 30
        сытость уменьшается на 10"""
        self.cat_satiety -= 10
        self.apartment.DIRT += 30

    def bad_games(self):
        """Кот портит обои. грязи прибавляется 5
        сытость уменьшается на 10"""
        self.cat_satiety -= 10
        self.apartment.DIRT += 5

    def print_info_cat(self):
        """Выводится информация о кошке"""
        print('Кот\n'
              'Имя: {}\n'
              'Сытость: {}\n'.format(self.name, self.cat_satiety))


