# TODO здесь писать код
import random
new_num = 0

with open('lucky_nums_file.txt', 'w', encoding='utf-8') as lucky_nums_file:
    try:
        while new_num <= 777:
            lucky_number = random.randint(1, 13)
            if lucky_number == 13:
                raise TypeError
            number = int(input('Введите число: '))
            lucky_nums_file.write(f'{number}\n')
            new_num += number
    except TypeError:
        print('Тебе не повезло!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')