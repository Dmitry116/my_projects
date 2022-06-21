num_list_1 = []
num_list_2 = []

for i in range(3):
    num_1 = int(input(f'Введите {i+1}-е число для первого списка: '))
    num_list_1.append(num_1)

for i in range(7):
    num_2 = int(input(f'Введите {i+1}-е число для первого списка: '))
    num_list_2.append(num_2)


print('Первый список: ', num_list_1)
print('Второй список: ', num_list_2)

num_list_1.extend((num_list_2))

print('Новый первый список с уникальными элементами:  ', set(num_list_1))

# TODO здесь писать код
#[1, 2, 3]
#[2, 4, 6, 3, 3, 2, 1]