nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

list_num = []

def separ_numbers(number):
    for num in number:
        if isinstance(num, list):
            separ_numbers(num)
        else:
            list_num.append(num)


separ_numbers(nice_list)
print(list_num)

# TODO здесь писать код
