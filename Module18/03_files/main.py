# TODO здесь писать код
invalid_symbol = ('@','№','$', '%', '^', '&', '*', '(', ')')
file_ext = ('.txt', '.docx')
file_name = input('Введите название файла: ')

if file_name.startswith(invalid_symbol):
    print('Ошибка: название начинается на один из специальных символов.')
elif not file_name.endswith(file_ext):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно. ')