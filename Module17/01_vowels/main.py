# TODO здесь писать код

text = input('Введите текст: ')
abc_list = ['а','е','и','о','у','ё','ю','я']
symbol = [i for i in text if i in abc_list]

print('Список гласных букв: ', symbol)
print('Длина списка: ', len(symbol))


