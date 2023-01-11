# TODO здесь писать код
import random


class Life_simulator:

    def one_day(self):
        with open('karma.log', 'w', encoding='utf-8') as karma:
            if random.randint(1, 10) == 1:
                karma.write(
                    random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']))
        return random.randint(1, 7)


karma_life = Life_simulator()
total_carma = 0

while total_carma <= 500:
    total_carma += karma_life.one_day()
    print(total_carma)
