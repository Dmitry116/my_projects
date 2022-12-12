# TODO здесь писать код
import random
class Potato:
    states = {0: 'Отсуствует',
              1: 'Росток',
              2: 'Зеленая',
              3: 'Зрелая'
              }

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class Gardener:
    name = 'Bob 🚶'
    life_count = 100
    damage = 20


class Pests:
    name = '🦗🐛🦗🐛🦗🐛'
    life_count = 100
    damage = 20
class Potato_garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def watering(self):
        potato_watering = input('Нужно полить картошку! Да или Нет: ').lower()
        if potato_watering == 'да' or potato_watering == 'lf':
            my_garde.pests()
        elif potato_watering == 'нет' or potato_watering == 'ytn':
            print('Ваша картошка погибла, так и не дождавшись воды...')
            raise SystemExit

    def pests(self):
        num_pests = random.randint(1, 3)
        if num_pests == 2:
            print('Напали вредители {}\n'.format(Pests.name))
            pests_control = input('Нужна ваша помощь!\n'
                                  'Помочь картошке? Да или Нет: ')
            if pests_control == 'да' or pests_control == 'lf':
                my_battle.combat_vs_pests()
            if pests_control == 'нет' or pests_control == 'ytn':
                print('Вашу картошку съели вредиели {}. Ваша деревня обречена!'.format(Pests.name))
                raise SystemExit
        else:
            my_garde.potato_patch()

    def potato_patch(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Вы справились со своими обязанностями!\n'
                  'Картошка созрела! Можно собирать.\n')
        else:
            print('Еще не созрела!\n')


class Combat:
    def combat_vs_pests(self):
        print('Да начнется битва...')
        man_life = Gardener.life_count
        pests_life = Pests.life_count
        print('Кол-во жизней садовника: ', man_life)
        print('Кол-во жизней вредителей: ', pests_life)
        next_step = input('Нажмите Enter\n')

        while True:
            print('Садовник {} нанес удар: {}'.format(Gardener.name, Gardener.damage))
            pests_life -= Gardener.damage
            if pests_life <= 0:
                print('Вы отбились от вредителей. Но они обещали вернуться...')
                my_garde.potato_patch()
                break
            elif pests_life < 40:
                pest_reinforcement = random.randint(1, 3)
                if pest_reinforcement == 1:
                    print('Кол-во жизней вредителей: ', pests_life)
                    print('Паразиты сбежали с поля битвы с большими потерями!\n')
                    my_garde.potato_patch()
                    break
                if pest_reinforcement == 3:
                    reinforcement_pests = 30
                    pests_life += reinforcement_pests
                    print(f'К отряу вредителей прибыло подкрепление +{reinforcement_pests}')
            print('Кол-во жизней вредителей: ', pests_life)

            print('Вредители {} нанесли удар: {}'.format(Pests.name, Pests.damage))
            man_life -= Pests.damage
            print('Кол-во жизней садовника: ', man_life)
            stop = input('Нажмите Enter\n')

            if man_life <= 0:
                print('Вы отважно сражались ... но безрезультатно. Паразиты торжествуют!')
                raise SystemExit

            elif man_life < 40:
                ans_man = input('Жизни стало меньше половины! Сбежать с поля битвы: Да или Нет').lower()
                if ans_man == 'да' or ans_man == 'lf':
                    print('Вы сбежали с поля битвы, бросив доверенную Вам картошку! Паразиты торжествуют!')
                    raise SystemExit
                if ans_man == 'нет' or ans_man == 'ytn':
                    man_reinforcement = random.randint(1, 3)
                    if man_reinforcement == 2:
                        reinforcement_man = 50
                        man_life += reinforcement_man
                        print(f'Баба Варя, ваша соседка принесла вам 🍺(это вода:)).\n'
                              f'Жизнь садовника увеличилась на {reinforcement_man}')






num_potatos = int(input('Сколько картошки будем сажать: '))
my_garde = Potato_garden(num_potatos)
my_battle = Combat()
print('На Вас возложенна большая миссия! \nСохраните картошку!')

for _ in range(3):
    my_garde.watering()  # полив картошки
    my_garde.are_all_ripe()
