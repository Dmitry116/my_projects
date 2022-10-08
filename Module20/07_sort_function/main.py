# TODO здесь писать код

def tpl_sort(numbers):
    num_float = False
    for i in numbers:
        if int(i) != i:
            num_float = True

    if num_float == True:
        return numbers
    else:
        return tuple(sorted(numbers))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
