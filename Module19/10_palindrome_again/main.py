# TODO здесь писать код

string = input('Введите строку: ')
a = string
for i in range(len(string)):
    a = a[1:] + a[:1]
    if a == a[::-1]:
        print('Можно сделать палиндромом')
        break
    print('Нельзя сделать палиндромом')
    break