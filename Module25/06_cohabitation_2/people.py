import random


class Human:
    """В __init__ параметры имя, apartment ссылка на класс Home,
    сытость по умолчанию 30, счастье по умолчанию 100"""

    def __init__(self, name, apartment, satiety=30, happy=100):
        self.name = name
        self.apartment = apartment
        self.human_satiety = satiety
        self.human_happy = happy

    def check_human_happy_satiety(self):

        """Проверка на сытость и счастье персонажа.
        если сытость меньше или равняется 0
        или если счастье меньше 10 то игра заканчивается"""

        if self.human_satiety <= 0:
            print(f'{self.name} умер(ла) от голода...\n'
                  f'Конец игры!')
            self.end_game()
        elif self.human_happy < 10:
            print(f'{self.name} умер(ла) от скуки...\n'
                  f'Конец игры!')
            self.end_game()

    def check_dirt(self):

        """Проверка на количество грязи в доме. если больше 100,
        настроение персонажа уменьшается на 10"""

        if self.apartment.DIRT >= 100:
            print(f'{self.name} страдает от грязного дома...')
            self.human_happy -= 10

    def human_eating(self):

        """Человек ест. сытость увеличивается на 30. Запасы еды уменьшаются на 30"""

        eating = 30
        if self.apartment.FOOD_HUMAN == 0:
            print('У людей закончилась еда!')
        elif self.apartment.FOOD_HUMAN < 30:
            eating = self.apartment.FOOD_HUMAN
            print(f'{self.name} поел... маловато будет.')
            self.human_satiety += eating
            self.apartment.FOOD_HUMAN -= eating
        else:
            print(f'{self.name} поел...')
            self.human_satiety += eating
            self.apartment.FOOD_HUMAN -= eating

    def takes_cats(self):

        """Когда берут кота, счастье увеличивается на 10
        кот иногда может царапаться. счастье уменьшается на 10
        сытость уменьшается на 10"""

        cat_mood = random.randint(1, 5)
        happy = 10
        self.human_satiety -= 10
        if cat_mood == 1:
            print('У кота плохое настроение, он царапается.\n'
                  f'настроение уменьшилось на: {happy}')
            self.human_happy -= happy
        else:
            print('Погладил кота.')
            self.human_happy += happy

    def print_info_human(self):

        """Выводит информацио о персонаже"""

        print('Имя: {}\n'
              '\033[31mСытость: {}\033[0m\n'
              'Счастье: {}\n'.format(self.name, self.human_satiety, self.human_happy))

    def end_game(self):
        print(f'Кол-во прожитых дней: {self.apartment.COUNT_DAYS}')
        raise SystemExit


class Husband(Human):

    def __init__(self, name, apartment):
        super().__init__(name, apartment, satiety=30, happy=100)

    def plays_pc(self):
        """Муж играет. Счастье увеличивается на 20
        сытость уменьшается на 10"""

        print('Поиграл на компьютере...')
        self.human_satiety -= 10
        self.human_happy += 20

    def going_work(self):
        """Муж идет на работу, зарплату приносит 150
        сытость уменьшается на 10"""

        print('Сходил на работу...')
        self.human_satiety -= 10
        self.apartment.MONEY += 150


class Wife(Human):
    """FUR_COAT количество шуб"""

    FUR_COAT = 0

    def __init__(self, name, apartment):
        super().__init__(name, apartment, satiety=30, happy=100)

    def going_shop(self):

        """Жена идет в магазин покупает еду для семьи и кошкам
        сытость уменьшается на 10"""

        self.human_satiety -= 10

    def buy_fur_coat(self):

        """Жена покупает шубу. бюджет тратится на 350, счастье увеличивается на 60
        сытость уменьшается на 10"""

        fur_coat = 350
        self.human_satiety -= 10
        if self.apartment.MONEY >= fur_coat:
            print(f'{self.name} купила себе шубу.')
            happy = 60
            Wife.FUR_COAT += 1
            self.apartment.MONEY -= fur_coat
            self.human_happy += happy
        else:
            print(f'{self.name} так хотела новую шубу и не смогла ее себе купить\n'
                  f'{self.name} очень растроена... ее настроение уменьшается на 20')
            self.human_happy -= 20

    def cleaning_home(self):

        """Жена убирается дома
        сытость уменьшается на 10"""

        self.human_satiety -= 10


class Child(Human):
    def __init__(self, name, apartment):
        super().__init__(name, apartment, satiety=30, happy=100)

    def human_eating(self):

        """Ребенок ест, сытость увеличивается на 20. запасы уменьшаются на 20"""
        eats = 20
        if self.apartment.FOOD_HUMAN == 0:
            print('У людей закончилась еда!')
        elif self.apartment.FOOD_HUMAN < eats:
            eating = self.apartment.FOOD_HUMAN
            print(f'{self.name} поел... маловато будет.')
            self.human_satiety += eating
            self.apartment.FOOD_HUMAN -= eating
        else:
            print(f'{self.name} поел...')
            self.human_satiety += eats
            self.apartment.FOOD_HUMAN -= eats

    def walks(self):

        """Ребенок ходит играть на улицу
        настроение повышается на 20, грязь в доме увеличивается на 10
        сытость уменьшается на 10"""

        self.human_satiety -= 10
        self.human_happy += 20
        self.apartment.DIRT += 10

    def going_school(self):

        """Ребенок ходит в школу. Уменьшается сытость на 10
        Уменьшается настроение на 10"""

        self.human_satiety -= 10
        self.human_happy -= 20
