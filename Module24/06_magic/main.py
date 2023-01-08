# TODO здесь писать код
import random


class Water:
    def __str__(self):
        water = 'Вода'
        return water

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()


class Air:
    def __str__(self):
        air = 'Воздух'
        return air

    def __add__(self, other):
        if isinstance(other, Earth):
            return Steam()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()


class Fire:
    def __str__(self):
        fire = 'Огонь'
        return fire

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()


class Earth:
    def __str__(self):
        earth = 'Земля'
        return earth

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()


class Storm:
    def __str__(self):
        storm = 'Шторм'
        return storm


class Steam:
    def __str__(self):
        steam = 'Пар'
        return steam


class Dirt:

    def __str__(self):
        dirt = 'Грязь'
        return dirt


class Dust:
    def __str__(self):
        dust = 'Пыль'
        return dust


class Lava:
    def __str__(self):
        lava = 'Лава'
        return lava


class Lightning:
    def __str__(self):
        lightning = 'Молния'
        return lightning


elements = {
    1: Water(),
    2: Air(),
    3: Fire(),
    4: Earth()
}

elem_1 = elements[random.randint(1, 4)]
elem_2 = elements[random.randint(1, 4)]
elem_3 = elem_1 + elem_2
print(f'{elem_1} + {elem_2} = {elem_3}')
print()
