# TODO здесь писать код
import random

N = int(input('Количество палок: '))
sticks = ['|' for _ in range(N)]
print(*sticks, sep = '')

K = int(input('Кол-во бросков: '))
for i in range(K):
    L_i = random.randint(0, N)
    R_i = random.randint(L_i, N)
    print(f'Бросок {i+1}. Сбиты палки с номера {L_i} по номер {R_i}.')

    for i in range(L_i, R_i):
       sticks[i] = '.'
    print(*sticks, sep = '')
print('Результат: ', *sticks, sep = '')
