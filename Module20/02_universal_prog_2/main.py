# TODO здесь писать код
def crypto(text):
    return [text[num]
     for num in range(len(text)) if num > 1
        and all(True if num % i != 0
            else False
               for i in range(2, num))]


print('Ответ', crypto('О Дивный Новый мир!'))
print('Ответ: ', crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
