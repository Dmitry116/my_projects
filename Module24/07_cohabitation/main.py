# TODO здесь писать код
from work_message import Work_message
from game_message import Game_message
import random


class Home:
    """Кол-во еды и денег у персонажей общее."""
    FOOD = 50
    MONEY = 0


class Human:

    def __init__(self, name, healphy, place_of_residence=None):
        self.name = name
        self.healphy = healphy
        self.apartment = place_of_residence

    def print_info(self):
        print('Имя: {}\n'
              'Здоровье: {}\n'
              'Кол-во денег: {}$\n'
              'Кол-во еды: {}\n'.format(self.name, self.healphy, self.apartment.MONEY, self.apartment.FOOD))

    def pests(self):
        '''Вредители уничтожают еду'''
        pests = random.randint(0, 2)
        if pests == 1:
            #Home.FOOD = 0
            self.apartment.FOOD = 0
            print('На кухне побывали вредители...\n'
                  'Съели всю еду.\n')

    def eat(self):
        '''Пополнение здоровья'''
        food = 20
        if self.apartment.FOOD <= 0:
            print('Еда закочилась!')

        elif self.apartment.FOOD < food:  # проверка чтобы еда не уходила в минус
            self.healphy += self.apartment.FOOD
            self.apartment.FOOD -= self.apartment.FOOD
            print(f'Сходил(а) на кухню, поел.\n'
                  f'Пополнил(а) здоровье на: {self.apartment.FOOD}\n'
                  f'Кол-во здровья: {self.healphy}\n'
                  f'Еды осталось: {self.apartment.FOOD}\n')
        else:
            self.healphy += food
            self.apartment.FOOD -= 20
            print(f'Сходил(а) на кухню, поел.\n'
                  f'Пополнил(а) здоровье на: {food}\n'
                  f'Кол-во здровья: {self.healphy}\n'
                  f'Еды осталось: {self.apartment.FOOD}\n')

    def work(self):
        '''Пополнение денег'''
        death = random.randint(1, 10)
        if death == 4:
            print(f'\033[31mВаш питомец {self.name} случайно погиб на работе...\033[0m')
            man.end_game()
        else:
            if self.healphy <= 0:
                print(f'\033[31mВаш питомец {self.name} умер от голода на работе...\033[0m')
                man.end_game()
            else:
                paid = random.randint(0, 2)
                money = Work_message.message[paid][1]
                healphy = 10
                self.apartment.MONEY += money
                self.healphy -= healphy
                print(f'{Work_message.message[paid][0]}\n'
                      f'Заработал денег: {money}$\n'
                      f'Потратил здоровье на работе: {healphy}\n'
                      f'Здровья осталось: {self.healphy}\n')

    def play(self):
        '''Обязательая игра'''
        game = random.randint(0, 2)
        healphy = Game_message.message[game][1]
        self.healphy -= healphy
        print(f'{Game_message.message[game][0]}\n')
        if self.healphy <= 0:
            if game == 1:
                print(f'Здоровья осталось: {self.healphy}')
                print(f'\033[31mВаш питомец {self.name} погиб при случайных обстоятельствах...\033[0m')
                man.end_game()
            else:
                print(f'\033[31mВаш питомец {self.name} умер от голода во время игры\033[0m')
                man.end_game()
        else:
            print(f'Потратил здоровье: {healphy}\n'
                  f'Здровья осталось: {self.healphy}\n')

    def shooping(self):
        '''Пополнение еды и возможное нападение грабителей'''
        robbers = random.randint(1, 5)
        food = 30
        money = 30
        # проверка наличия денег для покупки еды
        if self.apartment.MONEY < money:
            money = self.apartment.MONEY
            food = self.apartment.MONEY
        if robbers == 1:
            win = random.randint(0, 1)
            print('По дороге в магазин, напали грабители.\n')
            if win == 0:
                print('Отобрали все деньги и избили...\n')
                self.healphy -= 20
                self.apartment.MONEY = 0
                if self.healphy <= 0:
                    print(f'\033[31mВаш питомец {self.name} погиб возле магазина...\033[0m')
                    man.end_game()
                else:
                    self.eat()
            else:
                self.apartment.FOOD += food
                self.apartment.MONEY -= money
                print(f'Ваш питомец {self.name} смог отбиться от грабителей!\n'
                      f'Пополнил запасы еды на: {food}\n'
                      f'Потратил денег на еду: {money}$\n'
                      f'Кол-во еды: {self.apartment.FOOD}\n'
                      f'Кол-во денег: {self.apartment.MONEY}$\n')
                if self.healphy <= 20:
                    self.eat()
        else:
            self.apartment.FOOD += food
            self.apartment.MONEY -= money
            print(f'Сегодня поход в магазин прошел спокойно.\n'
                  f'Пополнил запасы еды на: {food}\n'
                  f'Потратил денег на еду: {money}$\n'
                  f'Кол-во еды: {self.apartment.FOOD}\n'
                  f'Кол-во денег: {self.apartment.MONEY}$\n')
            if self.healphy <= 20:
                self.eat()

    def end_game(self):
        '''Закрывает игру с выводом прожитых дней'''
        print(f'Кол-во прожитых совместных дней составило: {count_days}')
        raise SystemExit


new_apartment = Home()
man = Human('Артем', 50, new_apartment)
woman = Human('Мария', 50, new_apartment)

count_days = 1
while count_days != 10:
    print(f'\033[31mДень {count_days}-й.\033[0m')
    for people in (man, woman):

        next_step = input('Нажмите Enter чтобы продолжить.')
        people.print_info()
        if people.healphy <= 20:
            print('Хочу есть! ')
            people.eat()
        if new_apartment.FOOD <= 20:
            print('Пошел(а) за продуктами в магазин!')
            people.shooping()
        if new_apartment.MONEY <= 30:
            print('Мало денег. Надо найти работу!.')
            people.work()

        print('Снова игра!')
        people.play()
        people.pests()
    count_days += 1

print(f'Ваши питомцы сумели выжить!\n'
      f'Кол-во дней составило: {count_days}')
