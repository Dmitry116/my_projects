# TODO здесь писать код

def revers(n):
  numbers = 0
  num = str(n).split('.')
  a = str(num[0])
  b = str(num[-1])
  numbers = float(a[::-1] + '.' + b[::-1])
  return numbers

number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите первое число: '))
num_1 = revers(number_1)
num_2 = revers(number_2)
print('Первое число наоборот: ', num_1)
print('Второе число наоборот: ', num_2)
print('Сумма: ', num_1 + num_2)


