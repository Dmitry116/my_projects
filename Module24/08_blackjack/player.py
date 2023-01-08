import random
from cards import *


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    """Добавление карт игроку"""
    """Удаление карт из колоды"""

    def add_cards(self, player_cards):
        num = -1
        while num not in cards:
            num = random.randint(0, 51)
        self.cards.append(cards[num])  # добавляем карту игроку
        del cards[num]  # удаление карты из колоды которую добавили игроку

    def count_score(self):
        score = 0
        self.cards.sort(key=lambda x: x[1])
        for card in self.cards:
            if 'A' in card[0]:
                if score + card[1] > 21:
                    score += 1
                else:
                    score += card[1]
            else:
                score += card[1]
        return score

    def print(self):
        print(f'Имя: {self.name}\n'
              f'Карты: {[i[0] for i in self.cards]}\n'
              f'Кол-во очков: {self.count_score()}\n')
