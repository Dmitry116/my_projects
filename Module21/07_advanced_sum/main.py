# TODO здесь писать код
def summ_numbers(args):
    result = 0
    for value in args:
        if isinstance(value, (list, tuple)):
            result += summ_numbers(value)
        elif isinstance(value, int):
            result += value
    return result


num_1 = (1, 2, 3, 4, 5)
num_2 = ([[1, 2, [3]], [1], 3])
print('Ответ в консоли: ',summ_numbers(num_1))
print('Ответ в консоли: ',summ_numbers(num_2))






