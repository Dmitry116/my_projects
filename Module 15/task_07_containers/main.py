def get_input_parameters():
    print('Вес контейнера не должен превышать 200!')
    list_container_weights = []
    containers = int(input('Кол-во контейнеров: '))
    for i in range(containers):
        containers_weigth = int(input(f'Введите вес {i + 1} контейнера: '))
        list_container_weights.append(containers_weigth)

    print('Список весов контейнеров: ', list_container_weights)


    new_container_weight = int(input('Введите вес нового контейнера: '))


    return list_container_weights, new_container_weight

    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: ([165, 163, 160, 160, 157, 157, 155, 154], 162)
    :rtype: Tuple[List[int], int]
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем



def display_result(serial_number_new_container):

    print('Порядковый номер нового контейнера: ', serial_number_new_container)

    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем



def search_serial_number_new_container(list_container_weights, new_container_weight):

    if new_container_weight > 200:
        print('Вес контейнера больше 200, выберите другой контейнер!')
        get_input_parameters()

    else:
        list_container_weights.append((new_container_weight))
        list_container_weights.append(new_container_weight)
        list_container_weights.sort(reverse=True)
        serial_number_new_container = (list_container_weights.index(new_container_weight) + 1)

        return serial_number_new_container


    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    # TODO: в этой функции пишем логику поиска куда вставим новый контейнер.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result

    list_container_weights, new_container_weight = get_input_parameters()  # получаем параметры
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
