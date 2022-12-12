# TODO здесь писать код
import random


class Unit_1:
    name = 'Morpheus'
    health = 100
    damage = 20
    num = 1


class Unit_2:
    name = 'Agent Smith'
    health = 100
    damage = 20
    num = 2


class Fight:
    print('Начинается поединок между {} и {}'.format(Unit_1.name, Unit_2.name))
    print('Кол-во очков жизни {}: {}'.format(Unit_1.name, Unit_1.health))
    print('Кол-во очков жизни {}: {}'.format(Unit_2.name, Unit_2.health))
    print()
    while True:
        next_step = input('Нажмите Enter чтобы продолжить\n')
        if Unit_1.num == random.randint(1, 2):
            print('{} наносит удар: {}'.format(Unit_1.name, Unit_1.damage))
            Unit_2.health -= Unit_1.damage
        else:
            print('{} промахнулся.'.format(Unit_1.name))
        print('Кол-во очков жизни {}: {}'.format(Unit_2.name, Unit_2.health))
        if Unit_2.health <= 0:
            print('Кол-во очков жизни {}: {}'.format(Unit_2.name, Unit_2.health))
            print('Победитель: ', Unit_1.name)
            raise SystemExit

        if Unit_2.num == random.randint(1, 2):
            print('{} наносит удар: {}'.format(Unit_2.name, Unit_2.damage))
            Unit_1.health -= Unit_2.damage
        else:
            print('{} промахнулся.'.format(Unit_2.name))
        print('Кол-во очков жизни {}: {}'.format(Unit_1.name, Unit_1.health))
        if Unit_1.health <= 0:
            print('Кол-во очков жизни {}: {}'.format(Unit_1.name, Unit_1.health))
            print('Победитель: ', Unit_2.name)
            raise SystemExit


Fight()
