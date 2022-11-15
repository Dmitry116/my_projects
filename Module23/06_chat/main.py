# TODO здесь писать код
def read_chat():
    chat_file = open('history_chat.txt', 'r', encoding='utf-8')
    list_chat = [i for i in chat_file]
    if len(list_chat) == 0:
        print('Чат пуст')
    else:
        for i_text in list_chat:
            print(i_text, end='')
    print()
    chat_file.close()


def write_message():
    message = input('Введите текст сообщения: ')
    history_chat_file.write(f'{user}: {message}\n')
    history_chat_file.close()


choice_number = {
    1: 'Посмотреть текущий текст чата.',
    2: 'Отправить сообщение.'
}

while True:
    history_chat_file = open('history_chat.txt', 'a', encoding='utf-8')
    user = input('Как Вас зовут: ').capitalize()
    print(f'Здравствуйте {user}, выберите дальнейшее действие.')
    try:
        choice = int(input(f'Меню:\n'
                           f'{1} - Посмотреть текущий текст чата.\n'
                           f'{2} - Отправить сообщение.\n'))
        if choice == 1:
            read_chat()
        elif choice == 2:
            write_message()
    except ValueError:
        continue
