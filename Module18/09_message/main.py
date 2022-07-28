# TODO здесь писать код

text = input('Введите текст: ')

temp = ''
result = ''

for symbol in text:
    if symbol.isalpha():
        temp = symbol + temp
    else:
        result += temp + symbol
        temp = ''

result += temp

print('Новое сообщение: ', result)



