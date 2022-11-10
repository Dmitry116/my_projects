# TODO здесь писать код
import os


def save_file(file_name, file_path):
    # идет проверка на каталог
    if os.path.isdir(file_path) is True:
        # идет проверка на наличие файла
        file_path_name = os.path.join(file_path, file_name)
        if os.path.isfile(file_path_name) is True:
            print('Такой файл существует!')
            choice_file = input('Перезаписать его? Да или Нет: ').lower()
            # перезапись файла
            if choice_file == 'да' or choice_file == 'lf':
                overwrite_file()
            elif choice_file == 'нет' or choice_file == 'ytn':
                print('Программа закрывается! Всего хорошего!')
                raise SystemExit
        # создание файла
        else:
            create_file()

    # тут выбор если каталога нет
    # создать каталог или нет.
    else:
        print('Такого пути нет.')
        choice_dir = input('Создать каталог? Да или Нет: ').lower()
        if choice_dir == 'да' or choice_dir == 'lf':
            create_directory(file_path)
        elif choice_dir == 'нет' or choice_dir == 'ytn':
            print('Программа закрывается! Всего хорошего!')
            raise SystemExit


def overwrite_file():
    file_path_name = os.path.join(file_path, file_name)
    old_file = open(file_path_name, 'w')
    old_file.write('Перезапись файла!')
    old_file.close()
    print('Файл успешно перезаписан!')


def create_file():
    file_path_name = os.path.join(file_path, file_name)
    new_file = open(file_path_name, 'w')
    new_file.close()
    print('Файл успешно сохранён!')


def create_directory(path):
    os.makedirs(path)
    print('Каталог успешно создан!')
    save_file(file_name, file_path)


file_save = input('Куда хотите сохранить документ? '
                  '\nВведите последовательность папок (через пробел): ').split()
file_name = input('Введите имя файла и его расширение: ')
file_path = '\\' + '\\'.join(file_save)

save_file(file_name, file_path)
