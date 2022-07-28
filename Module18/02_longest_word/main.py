# TODO здесь писать код

words_str = input('Введите строку: ').split()

max_num = 0
max_word = ''
for word in words_str:
    if len(word) > max_num:
        max_word = word
        max_num = len(word)

print('Самое длинное слово: ', max_word)
print('Длина этого слова: ', max_num)
