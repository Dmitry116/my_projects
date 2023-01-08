# TODO здесь писать код

from player import Player

"""Запрос на добавление карты игроку"""


def more_cards():
    print(f'Игрок: {player_1.name}\nКарты: {[i[0] for i in player_1.cards]}')
    print(f'Кол-во очков: {Player.count_score(player_1)}\n')
    answer = input('Добавить еще карту? "да" или "нет": '.lower())
    if answer == 'да' or answer == 'lf':
        player_1.add_cards(player_1)


player_1 = Player('Артем')
player_2 = Player('Дилер')
players = player_1, player_2

for player in players:
    for _ in range(2):
        player.add_cards(player)

more_cards()

player_1.print()
player_2.print()

if Player.count_score(player_1) < Player.count_score(player_2) or Player.count_score(player_1) > 21:
    print('Аррем проиграл.')
elif Player.count_score(player_1) == Player.count_score(player_2):
    print('Ничья')
else:
    print('Артем выиграл.')
