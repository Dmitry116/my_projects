# TODO здесь писать код
import os


def gen_files_path(path):

    """a directory_path.log file is created, where the path to all directories is written
    os.walk(path) - traverses the entire directory at the specified path"""

    with open('directory_path.log', 'w', encoding='utf-8') as dir_path:
        for i_path in list(os.walk(path)):
            print(i_path)
            dir_path.write(str(f'{i_path}\n'))


directory_path = r'j:\test'
gen_files_path(directory_path)
