# TODO здесь писать код
import random




def one_day():

    if random.randint(1, 10) == 1:
        exception = random.choice((KillError, DrunkError, CarCrashError, GluttonyError, DepressionError))
        raise exception()
    return random.randint(1, 7)


class KillError(Exception):

    def __init__(self):
        super().__init__('Убийство. Вы и убили-с!')


class DrunkError(Exception):

    def __init__(self):
        super().__init__('Бухой!')


class CarCrashError(Exception):

    def __init__(self):
        super().__init__('Разбил машину!')


class GluttonyError(Exception):

    def __init__(self):
        super().__init__('Чревоугодие!')


class DepressionError(Exception):

    def __init__(self):
        super().__init__('Депрессия!')



total_carma = 0

while total_carma <= 500:
    try:
        total_carma += random.randint(1, 7)
        one_day()
        print(total_carma)
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as ex:
        with open('karma.log', 'w', encoding='utf-8') as karma:
            karma.write(str(ex))