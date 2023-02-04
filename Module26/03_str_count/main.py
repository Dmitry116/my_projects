# TODO здесь писать код
import os


# def gen_path(path):
#     """finds files (.py) in the specified directory"""
#     for i_path in os.walk(path):
#         for i_file in i_path[2]:
#             print(i_path[0])
#             if str(i_file).endswith('.py'):
#                 print(i_file)
#                 open_file(os.path.join(i_path[0], i_file))


def gen_path(path):
    """finds files (.py) in the specified directory"""

    for i_path in os.walk(path):
        for i_file in i_path[2]:
            if str(i_file).endswith('.py'):
                yield i_path
                print(open_file(os.path.join(i_path[0], i_file)))


def open_file(item):
    """opens files and counts the number of lines of code"""

    count = 0
    with open(item, 'r', encoding='utf-8') as file_py:
        for line_code in file_py:
            #print(line_code)
            if line_code == '\n' or line_code.startswith('"') or line_code.startswith('#'):
                continue
            else:
                count += 1
    return f'Total lines of code: {count}'


path_to_project = os.path.abspath(os.path.join('..', '..', 'Module14'))
gen = gen_path(path_to_project)
for i_path in gen:
    print(i_path[0])
