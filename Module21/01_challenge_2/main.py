# TODO здесь писать код

def print_numbers(start, num):
    if num <= 0:
        return 1
    print(start)
    start += 1
    return print_numbers(start, num-1)


start_num = 1
numbers = int(input('Введите число: '))
print_numbers(start_num, numbers)