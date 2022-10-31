# TODO здесь писать код
def num_fib(num):
    if num in (2, 1):
        return 1
    return num_fib(num - 1) + num_fib(num - 2)


num_position = int(input('Введите позицию числа в ряде Фибоначчи: '))
position = num_fib(num_position)
print('число', position)