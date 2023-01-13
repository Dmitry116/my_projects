
class Human:
    def __init__(self, name, satiety=30, happy=100, food_home=None):
        self.name = name
        self.human_satiety = satiety
        self.human_happy = happy
        self.home = food_home

    def human_eating(self):
        """Человек ест. сытость увеличивается на 30. Запасы еды уменьшаются на 30"""
        eating = 30
        self.human_satiety += eating
        self.home.FOOD_HUMAN -= eating

    def takes_cats(self):
        """Когда берут кота, счастье увеличивается на 10"""
        self.human_happy += 10

    def print_info_human(self):
        print('Имя: {}\n'
              'Сытость: {}\n'
              'Счастье: {}\n'.format(self.name, self.human_satiety, self.human_happy))


class Husband(Human):

    def __init__(self, name, food_home=None):
        super().__init__(name, satiety=30, happy=100)


    def palys_pc(self):
        """Муж играет. Счастье увеличивается на 20"""
        self.human_happy += 20

    def going_work(self):
        """Муж идет на работу, зарплату приносит 150"""
        pass


class Wife(Human):

    def __init__(self, name, food_home=None):
        super().__init__(name, satiety=30, happy=100)

    def going_shop(self):
        """Жена идет в магазин"""
        pass

    def buy_fur_coat(self):
        """Жена покупает шубу"""
        pass

    def cleaning_home(self):
        """Жена убирается дома"""
        pass


class Child(Human):
    def __init__(self, name, food_home=None):
        super().__init__(name, satiety=30, happy=100)

    def human_eating(self):
        self.eating = 20
