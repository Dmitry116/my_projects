# TODO здесь писать код
import os


def gen_files_path(path):
    with open('directory_path.log', 'w', encoding='utf-8') as dir_path:
        for i_path in list(os.walk(path)):
            print(i_path)
            dir_path.write(str(f'{i_path}\n'))


directory_path = r'j:\test'
gen_files_path(directory_path)
