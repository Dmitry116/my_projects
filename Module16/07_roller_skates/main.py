skates_list = []

skates = int(input('Сколько пар коньков: '))
for i in range(skates):
    skates_size = int(input(f'Размер {i+1}-й пары: '))
    skates_list.append(skates_size)

people_count = 0
people = int(input('Кол-во людей: '))
for i in range(people):
    people_size = int(input(f'Размер ноги {i+1}-го человека: '))
    if people_size in skates_list:
      people_count += 1
      skates_list.remove(people_size)



print('Наибольшее кол-во людей, которые могут взять ролики: ', people_count)

# TODO здесь писать код
