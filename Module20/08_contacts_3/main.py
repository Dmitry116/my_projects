phone_book = {}


def search_phone_book():
    find_surname = input('Введите фамилию для поиска: ').title()
    for key in phone_book:
        if find_surname in key:
            print("Абонент ", key, "  номер  ", phone_book[key])


def check_phone_book():
    man_data = input('Введите имя и фамилию нового контакта (через пробел): ').title()
    if len(phone_book) == 0:
        return write_phone_book(man_data)
    else:
        if man_data in phone_book:
            print('Такой человек уже есть в контактах.')
            choice()
        else:
            return write_phone_book(man_data)


def write_phone_book(man_data):
    number_phone = input('Введите номер телефона: ')
    phone_book[man_data] = number_phone


def choice():
    num = int(input('\n1 - Добавить контакт'
                    '\n2 - Найти Человека'
                    '\nВыберите номер действия: '))
    if num == 1:
        check_phone_book()
    elif num == 2:
        search_phone_book()


while True:
    choice()
    for key, value in phone_book.items():
        print(key, value)
