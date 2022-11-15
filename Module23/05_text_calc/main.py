# TODO здесь писать код


def symbols_check(i_data, num_list):
    temp_data = i_data.split()
    if len(temp_data[1]) != 1:
        question = input(f'Обнаружена ошибка в строке: {temp_data} Хотите исправить? Да или Нет ').lower()
        if question == 'да' or question == 'lf':
            answer = input('Введите исправленную строку через пробел: ')
            symbols_check(answer, num_list)
        elif question == 'нет' or question == 'ytn':
            raise ValueError
    if temp_data[1] == '+':
        num_list.append(int(temp_data[0]) + int(temp_data[2]))
    elif temp_data[1] == '-':
        num_list.append(int(temp_data[0]) - int(temp_data[2]))
    elif temp_data[1] == '*':
        num_list.append(int(temp_data[0]) * int(temp_data[2]))
    elif temp_data[1] == '/':
        num_list.append(int(temp_data[0]) / int(temp_data[2]))
    return num_list


num_list = []
with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for i_data in calc_file:
        try:
            print(i_data)
            symbols_check(i_data, num_list)
        except ValueError:
            pass
print('ress', sum(num_list))



