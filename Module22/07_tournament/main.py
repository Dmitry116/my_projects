# TODO здесь писать код


def unpacking_file(first_file):
    players_list = [i_name.split() for i_name in first_file]
    players_list.pop(0)
    players_list.sort(key=lambda test_list: test_list[2],  reverse=True)
    save_players(players_list)


def save_players(first_list):
    num_players = int(input('Сколько игроков вывести: '))
    second_tour = open('second_tour.txt', 'w')
    print(num_players)
    second_tour.write(str(num_players))
    for player in range(num_players):
        print(f'{player + 1}) {first_list[player][1][0]}. {first_list[player][0]} {first_list[player][2]}')
        second_tour.write(f'\n{player + 1}) {first_list[player][1][0]}. {first_list[player][0]} {first_list[player][2]}')

first_tour = open('first_tour.txt', 'r')



unpacking_file(first_tour)


