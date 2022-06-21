class_a = []
for i in range(160, 176, 2):
    class_a.append(i)

class_b = []
for i in range(162, 180, 3):
    class_b.append(i)

class_a.extend(class_b)
class_a.sort()
print('Отсортированный список учеников: ', class_a)




# TODO здесь писать код
