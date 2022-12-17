# TODO здесь писать код
from work_message import Work_message
from game_message import Game_message
import random




class Human:
    FOOD = 50
    MONEY = 0


    def __init__(self, name, healphy):
        self.name = name
        self.healphy = healphy


    def print_info(self):
        print('Имя: {}\n'
              'Здоровье: {}\n'
              'Кол-во денег: {}$\n'
              'Кол-во еды: {}\n'.format(self.name, self.healphy, Human.MONEY, Human.FOOD))

    '''Вредители уничтожают еду'''

    def pests(self):
        pests = random.randint(0, 2)
        if pests == 1:
            Human.FOOD = 0
            print('На кухне побывали вредители...\n'
                  'Съели всю еду.\n')

    '''Пополнение здоровья'''

    def eat(self):
        food = 20
        if Human.FOOD <= 0:
            print('Еда закочилась!')

        elif Human.FOOD < food:  # проверка чтобы еда не уходила в минус
            self.healphy += Human.FOOD
            Human.FOOD -= Human.FOOD
            print(f'Сходил(а) на кухню, поел.\n'
                  f'Пополнил(а) здоровье на: {Human.FOOD}\n'
                  f'Кол-во здровья: {self.healphy}\n'
                  f'Еды осталось: {Human.FOOD}\n')
        else:
            self.healphy += food
            Human.FOOD -= 20
            print(f'Сходил(а) на кухню, поел.\n'
                  f'Пополнил(а) здоровье на: {food}\n'
                  f'Кол-во здровья: {self.healphy}\n'
                  f'Еды осталось: {Human.FOOD}\n')

    '''Пополнение денег'''

    def work(self):
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
                Human.MONEY += money
                self.healphy -= healphy
                print(f'{Work_message.message[paid][0]}\n'
                      f'Заработал денег: {money}$\n'
                      f'Потратил здоровье на работе: {healphy}\n'
                      f'Здровья осталось: {self.healphy}\n')

    '''Обязательая игра'''

    def play(self):
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

    '''Пополнение еды и возможное нападение грабителей'''

    def shooping(self):
        robbers = random.randint(1, 5)
        food = 30
        money = 30
        # проверка наличия денег для покупки еды
        if Human.MONEY < money:
            money = Human.MONEY
            food = Human.MONEY
        if robbers == 1:
            win = random.randint(0, 1)
            print('По дороге в магазин, напали грабители.\n')
            if win == 0:
                print('Отобрали все деньги и избили...\n')
                self.healphy -= 20
                Human.MONEY = 0
                if self.healphy <= 0:
                    print(f'\033[31mВаш питомец {self.name} погиб возле магазина...\033[0m')
                    man.end_game()
                else:
                    self.eat()
            else:
                Human.FOOD += food
                Human.MONEY -= money
                print(f'Ваш питомец {self.name} смог отбиться от грабителей!\n'
                      f'Пополнил запасы еды на: {food}\n'
                      f'Потратил денег на еду: {money}$\n'
                      f'Кол-во еды: {Human.FOOD}\n'
                      f'Кол-во денег: {Human.MONEY}$\n')
                if self.healphy <= 20:
                    self.eat()
        else:
            Human.FOOD += food
            Human.MONEY -= money
            print(f'Сегодня поход в магазин прошел спокойно.\n'
                  f'Пополнил запасы еды на: {food}\n'
                  f'Потратил денег на еду: {money}$\n'
                  f'Кол-во еды: {Human.FOOD}\n'
                  f'Кол-во денег: {Human.MONEY}$\n')
            if self.healphy <= 20:
                self.eat()

    '''Закрывает игру с выводом прожитых дней'''

    def end_game(self):
        print(f'Кол-во прожитых совместных дней составило: {count_days}')
        raise SystemExit


man = Human('Артем', 50)
woman = Human('Мария', 50)


count_days = 1
day = 'день'
while count_days != 10:
    print(f'\033[31mДень {count_days}-й.\033[0m')
    for people in (man, woman):

        #next_step = input('Нажмите Enter чтобы продолжить.')
        people.print_info()
        if people.healphy <= 20:
            print('Хочу есть! ')
            people.eat()
        if Human.FOOD <= 20:
            print('Пошел(а) за продуктами в магазин!')
            people.shooping()
        if Human.MONEY <= 30:
            print('Мало денег. Надо найти работу!.')
            people.work()

        print('Снова игра!')
        people.play()
        people.pests()
    count_days += 1


print(f'Ваши питомцы сумели выжить!\n'
      f'Кол-во дней составило: {count_days}')
