# TODO здесь писать код
symbol_count = 0
num_str = 1

with open('people.txt', 'r', encoding='utf-8') as people_file:
    for i_name in people_file:
        try:
            check_name = i_name.replace('\n', '')
            if len(check_name) < 3:
                symbol_count += len(check_name)
                raise TypeError
            else:
                symbol_count += len(check_name)
            num_str += 1
        except TypeError:
            print('Ошибка: строка: {}. Имя: {}'.format(num_str, i_name))
print('Общее количество символов: {}.'.format(symbol_count))