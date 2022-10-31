# TODO здесь писать код

def summ_numbers(args):
    result = 0
    for value in args:
        if isinstance(value, list|tuple):
            result += summ_numbers(value)
        elif isinstance(value, int):
            result += value
    return result


num_1 = (1, 2, 3, 4, 5)
num_2 = ([[1, 2, [3]], [1], 3])
print(summ_numbers(num_1))
print(summ_numbers(num_2))


def my_sum(args):
    total = 0
    for sub_list in args:
        if isinstance(sub_list, list|tuple):
            total += my_sum(sub_list)
        else:
            total += sub_list
    return total


# total = my_sum(1, 2, 3, 4, 5)
total = my_sum([[1, 2, [3]], [1], 3])

print(f"Ответ в консоли: {total}")





