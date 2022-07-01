# TODO здесь писать код
abc_list = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))


chipher = [(abc_list[(abc_list.index(symbol) + shift) % 33]) if symbol != ' ' else ' '
           for symbol in text]

print('Зашифрованное сообщение: ', *chipher, sep = '')