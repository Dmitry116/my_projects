import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')

with open('coordinates.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                file_2 = open('result.txt', 'w')
                my_list = sorted([res1, res2, number])
                print('my_list', my_list)
                file_2.write(str(my_list))
            except TypeError:
                print("Неподдерживаемый тип данных!")
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')
        finally:
            file_2.close()



# TODO отредактировать и исправить программу
