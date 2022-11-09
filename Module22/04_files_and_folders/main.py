# TODO здесь писать код
import os


def search_folder(path, name):
    for i_name in os.listdir(path):
        if i_name == name:
            path_folder = path + '\\' + i_name
            print(path_folder)
            numbers_folder_file(path_folder)
        else:
            if os.path.isdir(path + '\\' + i_name):
                search_folder(path + '\\' + i_name, name)


def numbers_folder_file(path_folder):
    count_folder = 0
    count_file = 0
    bytes_file = 0
    for i_name in os.scandir(path_folder):
        if i_name.is_file():
            bytes_file += os.path.getsize(path_folder)
            count_file += 1
        if i_name.is_dir():
            count_folder += 1
            for i_file in os.scandir(i_name):
                if i_file.is_file():
                    bytes_file += os.path.getsize(i_file)
                    count_file += 1
    print('Размер каталога (в Кб): ', bytes_file / 1024)
    print('Количество подкаталогов: ', count_folder)
    print('Количество файлов: ', count_file)


name = 'Module14'
path = 'd:\\python'
search_folder(path, name)

# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15
