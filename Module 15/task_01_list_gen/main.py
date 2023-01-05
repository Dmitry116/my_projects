def get_input_parameters():

    n = int(input('Введите число: '))
    return n

def display_result(odd_numbers):

    print(odd_numbers)

def get_odd_numbers(n):

    number_list = []
    for num in range(1, n + 1, 2):
        number_list.append(num)

    return number_list

if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
