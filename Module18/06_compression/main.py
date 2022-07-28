# TODO здесь писать код

str_symbol = input('Введите строку: ')

result = ''
count = 1

for index in range(1, len(str_symbol)):
    if str_symbol[index-1] == str_symbol[index]:
        count += 1
    else:
        result += (str_symbol[index - 1]) + (str(count))
        count = 1
result += str_symbol[-1] + str(count)

print(result)


