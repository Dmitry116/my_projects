violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_play_list = []
play = int(input('Сколько песен выбрать? '))

for a in range(play):
    count = 0
    song = input(f'Название {a + 1} песни: ')
    for i in violator_songs:
        if song in i:
            new_play_list.append(violator_songs[count][1])
        count += 1

minuts = 0
for min in new_play_list:
    minuts += min

print('Общее время звучания песен:', round(minuts, 2))

