import random
from cards import Cards


class Player:
    count_points = {}

    def __init__(self, name):
        self.name = name
        self.cards = []

    """Добавление карт игроку"""
    """Удаление карт из колоды"""

    def add_cards(self, player_cards):
        num = random.randint(0, 51)
        if not num in Cards.cards:  # если карты нет в колоде, запускается рекурсия
            self.add_cards(player_cards)
        else:
            self.cards.append(Cards.cards[num])  # добавляем карту игроку
            if self.name in Player.count_points:
                Player.count_points[self.name] += Cards.cards[num][1]  # добавляются очки карты игроку
            else:
                Player.count_points[self.name] = Cards.cards[num][1]  # добавляются очки карты игроку
            del Cards.cards[num]  # удаление карты из колоды которую добавили игроку

    def print(self):
        print(f'Имя: {self.name}\n'
              f'Карты: {[i[0] for i in self.cards]}\n'
              f'Кол-во очков: {self.count_points[self.name]}\n')

    def __str__(self):
        return f'{self.name}'
