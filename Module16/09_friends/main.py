friends = int(input('Кол-во друзей:'))
iou = int(input('Долговых расписок: '))

friends_list = []

for i in range(friends):
    friends_list.append(0)

for i in range(iou):
    print(f'{i + 1}-я расписка ')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_money = int(input('Сколько: '))

    friends_list[to_whom - 1] -= how_money
    friends_list[from_whom - 1] += how_money

count = 0
print('\nБаланс друзей: ')
for i in friends_list:
    print(f'{count + 1}: {i}')
    count += 1

