# TODO здесь писать код
num = int(input('Введите максимальное число: '))
numbers = set(range(1, num+1))
number_list = set()

while True:
    question = input('Нужное число есть среди вот этих чисел: ')
    if question == 'Помогите!':
        sort_num = sorted(number_list)
        print('Артём мог загадать следующие числа: ', *sort_num)
        break

    a = [int(x) for x in question.split()]
    for i_num in a:
        if i_num not in numbers:
            print(f'Ошибка! Число {i_num} больше: {num}')
            raise SystemExit

    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        question = {number_list.add(i) for i in question.split()}
    elif answer == 'Нет':
        question = {number_list.discard(i) for i in question.split()}




