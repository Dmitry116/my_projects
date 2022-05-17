# TODO здесь писать код
number = int(input('Введите число: '))
divider = 1
while divider <= number:
  divider = divider + 1
  if number % divider == 0:
    print('Наименьший делитель, отличный от единицы: ', divider)
    break