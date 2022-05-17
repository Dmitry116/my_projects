# TODO здесь писать код
n = int(input('Введите число: '))
count_1 = 0
count_2 = 0
while n != 0:
    count_1 += n % 10
    count_2 += 1
    n //= 10
print('Сумма чисел: ', count_1)
print('Количество цифр в числе: ', count_2)
print('Разность суммы и количества цифр: ', count_1 - count_2)