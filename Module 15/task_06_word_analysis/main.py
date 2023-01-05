
def get_input_parameters():

    word = input('Введите влово: ')
    return word


    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем



def display_result(number_unique_letters):

    print('Количество уникальных букв в слове', number_unique_letters)


    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем



def count_number_unique_letters(word):

    print(word)
    number_unique_letters = 0
    for letter in word:
        count = 0
        for i in word:
            if letter == i:
              count += 1
        if count == 1:
            number_unique_letters += 1


    return number_unique_letters

    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """
    # TODO: в этой функции пишем логику считаем количество уникальных букв в слове.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.



if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
