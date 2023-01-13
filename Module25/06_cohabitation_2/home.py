class Home:
    MONEY = 100
    FOOD_HUMAN = 50
    FOOD_CATS = 30
    DIRT = 0

    def print_info_home(self):
        print('Запасы в доме:\n'
              'Деньги: {}\n'
              'Еда людей: {}\n'
              'Еда кошек: {}\n'
              'Загрязнение в доме: {}\n'.format(self.MONEY, self.FOOD_HUMAN, self.FOOD_CATS, self.DIRT))
