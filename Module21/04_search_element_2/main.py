# TODO здесь писать код

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search_element(data, tag, num=0):
    result = None
    if flag == True:
        if num == number:
            return result
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag, num +1)
    if result:
        return result

question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if question == 'y':
    number = int(input('Введите максимальную глубину: '))
    flag = True
elif question == 'n':
    flag = False

search_key = input('Искомый ключ: ')
value = search_element(site, search_key)

if value:
    print('Значение: ', value)
else:
    print('Значение ключа: ', value)