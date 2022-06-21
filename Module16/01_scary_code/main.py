a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count = 0
for i in a:
  if i == 5:
    count += 1
    a.remove(5)
print('Кол-во цифр 5 при первом объединении: ', count)

a.extend(c)
for i in a:
  if i == 5:
    count += 1
print('Кол-во цифр 3 при первом объединении: ', count)
print(a)

# TODO переписать программу
