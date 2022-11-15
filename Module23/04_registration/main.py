# TODO здесь писать код
def check_file(data_file):
    new_file = data_file.split()
    if len(new_file) != 3:
        raise IndexError
    if not new_file[0].isalpha():
        raise NameError
    if not '@' in new_file[1] and not '.' in new_file[1]:
        raise SyntaxError
    if not int(new_file[2]) in range(10, 100):
        raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as data_people, \
        open('registrations_bad.log', 'w', encoding='utf-8') as bad_data, \
        open('registrations_good.log', 'w', encoding='utf-8') as good_data:
    count_string = 1
    for data_file in data_people:
        if len(data_file.split()) > 0:
            try:
                check_file(data_file)
            except IndexError:
                bad_data.write(f'Строка {count_string} НЕ присутствуют все три поля: {data_file}\n')
            except NameError:
                bad_data.write(f'Строка {count_string} Поле имени содержит НЕ только буквы: {data_file}\n')
            except SyntaxError:
                bad_data.write(f'Строка {count_string} Поле «Имейл» НЕ содержит @ и .(точку): {data_file}\n')
            except ValueError:
                bad_data.write(f'Строка {count_string} Поле «Возраст» НЕ является числом от 10 до 99: {data_file}\n')
            else:
                good_data.write(f'{data_file}\n')
        else:
            bad_data.write(f'Строка {count_string} Пустая строка: {data_file}\n')

        count_string += 1
