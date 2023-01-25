# TODO здесь писать код
import random
import math


class Auto:
    def __init__(self, Y=0, X=0, angle=0, dist=0):
        self.Y = Y
        self.X = X
        self.angle = angle / 57.2958
        self.dist = dist
        self.count_dist = 0

    def move(self):

        """Задает координаты автомобилю"""

        self.Y = int(input('Введите координаты Y: '))
        self.X = int(input('Введите координаты X: '))
        self.angle = int(input('Введите угол поворота автобуса: '))
        self.dist = int(input('Введите дистанцию проезда: '))
        self.count_dist += self.dist

    def arrived(self):

        """Выводит координаты авотмобиля"""

        print('Координаты Y: ', self.Y + self.dist * math.cos(self.angle))
        print('Координаты X: ', self.X + self.dist * math.sin(self.angle))


class Bus(Auto):
    """bus_stop_passenger - хранятся данные сколько и на какой остановке сели пассажиры.
    ключ - остановка, значение - пассажиры"""

    def __init__(self, Y=0, X=0, angle=0, dist=0):
        super().__init__(Y=0, X=0, angle=0, dist=0)
        self.total_money = 0
        self.count_passengers = 0
        self.bus_stop_passenger = {}
        self.count_bus_stop = 0

    def bus_drive(self):

        bus.move()


    def input(self, num_bus_stop):

        """Рандомное кол-во пассажиров садится
         self.count_passengers - общее кол-во пассажиров в автобусе в данный момент
         self.bus_stop_passenger - зписывает остановку и кол-во пассажиров в словарь"""

        self.passengers = random.randint(5, 10)
        print(f'Зашло пассажиров: {self.passengers}\n')
        self.count_passengers += self.passengers
        self.bus_stop_passenger[num_bus_stop] = [self.passengers, 0]

    def output_and_pay(self):

        """Пассажиры выходят из автобуса и оплачивают проезд. запускается цикл.
        bus_stop_money - кол-во денег запаченных за проезд
        total_out_passengers - кол-во пассажиров вышедших на остоновке
        ticket - вычисление суммы за проезд. сколько проехал пассажир
                                            (чем дальше едет тем больше платит."""
        bus_stop_money = 0
        total_out_passengers = 0
        for key_bus_stop in self.bus_stop_passenger:
            self.bus_stop_passenger[key_bus_stop][1] += 1
            ticket = 5 * self.bus_stop_passenger[key_bus_stop][1]
            passenger_out = random.randint(1, 5)
            if passenger_out > self.bus_stop_passenger[key_bus_stop][0]:
                passenger_out = self.bus_stop_passenger[key_bus_stop][0]
                self.bus_stop_passenger[key_bus_stop][0] -= passenger_out
                bus_stop_money += ticket * passenger_out
                total_out_passengers += passenger_out
            else:
                bus_stop_money += ticket * passenger_out
                self.bus_stop_passenger[key_bus_stop][0] -= passenger_out
                total_out_passengers += passenger_out
        self.total_money += bus_stop_money
        self.count_passengers -= total_out_passengers
        print(f'Вышло пассажиров: {total_out_passengers}')
        print(f'Всего заплатили за проезд: {bus_stop_money}')

    def print_bus_info(self):
        print(f'Пройдено расстояние: {self.count_dist}\n'
            f'Общее кол-во денег: {self.total_money}\n'
            f'Общее кол-во пассажиров в автобусе: {self.count_passengers}\n')


"""Цикл кол-во остановок. num_bus_stop - название автобусной остановки (ключ) для словаря"""
num_bus_stop = 1
bus = Bus()
print(f'Остановка: {num_bus_stop}')
bus.input(num_bus_stop)

for _ in range(4):
    enter = input('Нажмите enter')
    num_bus_stop += 1
    bus.bus_drive()
    print('Автобус находится:')
    bus.arrived()
    print(f'Остановка: {num_bus_stop}')
    bus.output_and_pay()
    bus.input(num_bus_stop)
    bus.print_bus_info()
