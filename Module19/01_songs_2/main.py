def get_input_parameters():
    num = int(input('Сколько песен выбрать? '))
    return num

def num_song_count(num):
    song_len = 0
    for i_song in range(1, num+1):
        song = input(f'Название {i_song}-й песни: ')
        song_len += violator_songs[song]
    return song_len

def display_result(song_numbers):
    print(f'Общее время звучания песен: {round(song_numbers, 2)} минуты')

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
number = get_input_parameters()
song_numbers = num_song_count(number)
display_result(song_numbers)


# TODO здесь писать код
