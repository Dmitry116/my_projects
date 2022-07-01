# TODO здесь писать код
text = input('Введите строку: ')
first_h = text.find('h')
second_h = text.rfind('h')

print('Развёрнутая последовательность между первым и по'
      'следним h: ', text[first_h+1:second_h][::-1])