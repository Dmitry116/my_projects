# TODO здесь писать код
import os


def gen_files_path(path):

    """создается файл directory_path.log куда записывается путь всех каталогов
    os.walk(path) - проходит по всему каталогу указанному пути"""

    with open('directory_path.log', 'w', encoding='utf-8') as dir_path:
        for i_path in list(os.walk(path)):
            print(i_path)
            dir_path.write(str(f'{i_path}\n'))


directory_path = r'j:\test'
gen_files_path(directory_path)
