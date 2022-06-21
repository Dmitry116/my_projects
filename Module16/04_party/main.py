guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:

    guests_count = 0
    for i in range(len(guests)):
        guests_count += 1
    print(f'Сейчас на вечеринке {guests_count} человек: {guests}')

    guest_come = input('Гость пришел или ушел? ')

    if guest_come == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    new_guest = input('Имя гостя: ')

    if guests_count == 6:
        print(f'Прости, {new_guest}, но мест нет.')
        print()
        guest_come = input('Гость пришел или ушел? ')
        if guest_come == 'ушел':
            new_guest = input('Имя гостя: ')
            print(f'Пока, {new_guest}!')
            guests.remove(new_guest)
            print()
    else:
        if guest_come == 'пришел':
            print(f'Привет {new_guest}!')
            guests.append(new_guest)
        elif guest_come == 'ушел':
            print(f'Пока, {new_guest}!')
            guests.remove(new_guest)
    print()
