people = int(input('Кол-во человек: '))
dropped = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', dropped, 'человек.')

piople_circle = []
for i in range(people):
    piople_circle.append(i + 1)

out = 0

for _ in range(people - 1):
    print('\nТекущий круг людей', piople_circle)
    start = out % len(piople_circle)
    out = (start + dropped - 1) % len(piople_circle)
    print('Начало счёта с номера', piople_circle[start])
    print('Выбывает человек под номером', piople_circle[out])
    piople_circle.remove(piople_circle[out])

print('\nОстался человек под номером', piople_circle)