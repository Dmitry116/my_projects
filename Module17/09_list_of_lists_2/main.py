nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [numeral for i in nice_list[:len(nice_list)] for num in i for numeral in num]

print('Ответ: ', new_list)

# TODO здесь писать код
