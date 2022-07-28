# TODO здесь писать код
while True:
    def incorect_passowd():
        print('Пароль ненадёжный. Попробуйте ещё раз.\n')

    print('Пароль должен состоять минимум из восьми символов, \n'
          'в нём должны быть хотя бы одна большая буква и хотя бы три цифры.\n')

    password = input('Придумайте пароль: ')


    if len(password) < 8:
        incorect_passowd()
    elif sum(1 for c in password if c.isupper()) < 1:
        incorect_passowd()
    elif sum(1 for c in password if c.isdigit()) < 3:
        incorect_passowd()

    else:
        print('Это надёжный пароль!')
        break