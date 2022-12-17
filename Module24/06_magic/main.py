# TODO здесь писать код

elements = {
    1: 'Вода',
    2: 'Воздух',
    3: 'Огонь',
    4: 'Земля'
}

"""
Вода + Воздух = Шторм
Вода + Огонь = Пар
Вода + Земля = Грязь
Воздух + Огонь = Молния
Воздух + Земля = Пыль
Огонь + Земля = Лава
"""

class Water:
    print('Вода')

class Air:
    print('Воздух')

class Fire:
    print('Огонь')

class Ground:
    print('Земля')

water = Water()
air = Air()
fire = Fire()
ground = Ground()

class Example_1:
    def __add__(self, other):
        return Example_2()


class Example_2:
    answer = 'сложили два класса и вывели'


a = Example_1()
d = Example_1()
b = Example_2()

s = Example_2()
c = a + s
print(c.answer)