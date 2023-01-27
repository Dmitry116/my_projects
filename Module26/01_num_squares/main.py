# TODO здесь писать код
class Iterator_number:

    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__stop_iter = 0

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> int:
        if self.__stop_iter < self.__limit:
            self.__stop_iter += 1
            return self.__stop_iter ** 2
        raise StopIteration


def iterator_number(num):
    for number in range(1, num + 1):
        yield number ** 2


number = int(input('Введите число: '))

print('\nкласс-итератор')
iterator_num = Iterator_number(limit=number)
for i_num in iterator_num:
    print(i_num, end=' ')

print('\nфункция-генератор')
for i in iterator_number(number):
    print(i, end=' ')

print('\nгенераторное выражение')
num_gen = [num ** 2 for num in range(1, number + 1)]
print(num_gen)
