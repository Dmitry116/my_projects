# TODO здесь писать код
import os


def gen_path(path):
    """находит фалы (.py) по указанной директории """
    for i_path in os.walk(path):
        for i_file in i_path[2]:
            print(i_path[0])
            if str(i_file).endswith('.py'):
                print(i_file)
                open_file(os.path.join(i_path[0], i_file))


def open_file(item):
    """открывает файлы и считает кол-во строк кода"""
    count = 0
    with open(item, 'r', encoding='utf-8') as file_py:
        for line_code in file_py:
            print(line_code)
            if line_code == '\n' or line_code.startswith('"') or line_code.startswith('#'):
                continue
            else:
                count += 1
    print(f'Всего строк кода: {count}')


path_to_project = os.path.abspath(os.path.join('..', '..', 'test'))
gen_path(path_to_project)
