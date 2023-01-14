class Home:
    MONEY = 100
    FOOD_HUMAN = 50
    FOOD_CATS = 30
    DIRT = 0
    COUNT_DAYS = 0
    GAME = True

    def print_info_home(self):
        print('Запасы в доме:\n'
              'Деньги: {}\n'
              '\033[31mЕда людей: {}\033[0m\n'
              'Еда кошек: {}\n'
              'Загрязнение в доме: {}\n'.format(self.MONEY, self.FOOD_HUMAN, self.FOOD_CATS, self.DIRT))

    def dirt_every_day(self):
        self.DIRT += 5
