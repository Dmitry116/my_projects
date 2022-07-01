# TODO здесь писать код
import random

num = int(input('Количество чисел в списке: '))
nums = [random.randint(0, 2) for _ in range(num)]


print('Список до сжатия: ', nums)

nums_list = [x for x in nums if x > 0]


print('Список после сжатия: ', nums_list)
