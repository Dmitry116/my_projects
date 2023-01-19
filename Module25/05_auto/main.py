# TODO здесь писать код
import random
class Auto:
    def __init__(self, speed=None, odometr=None, fuel=None):
        self.speed = speed
        self.odometr = odometr
        self.fuel = fuel


class Bus(Auto):
    def __init__(self, speed=None, odometr=None, fuel=None):
        super().__init__(speed, odometr, fuel)
        self.money = 0
        self.count_passengers = 0

    def input(self):
        passengers = random.randint(1, 5)
        fare = 5
        self.count_passengers += passengers
        self.money += fare * passengers
        print(f'Вошло пассажиров: {passengers}')

    def output(self):
        passengers = random.randint(1, 5)
        if self.count_passengers < passengers:
            passengers = self.count_passengers
            print(f'Вышло пассажиов: {passengers}')

        else:
            self.count_passengers -= passengers
            print(f'Вышло пассажиов: {passengers}')


    def print_bus_info(self):
        print(f'Колличество денег: {self.money}\n'
              f'Колличество пассажиров: {self.count_passengers}')

bus = Bus()
bus.input()
bus.print_bus_info()
