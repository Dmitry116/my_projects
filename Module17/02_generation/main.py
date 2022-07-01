# TODO здесь писать код

n = int(input('Введите длину списка: '))
num = [(1 if i % 2 == 0 else i % 5) for i in range(n)]
print('Результат: ', num)
