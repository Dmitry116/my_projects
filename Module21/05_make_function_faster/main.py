def factorial(num):
    if num == 1:
        return num
    num_fact = factorial(num-1)
    return num * num_fact


def divizion_num(num, num_2):
    num_dvzn = num / (num_2 ** 3)
    return num_dvzn


def exp(num_dvzn):
    result = num_dvzn ** 10
    return result


def display(result):
    print(result)


number = 3
num_fact = factorial(number)
division = divizion_num(num_fact, number)
exp_num = exp(division)
display(exp_num)


# TODO оптимизировать функцию
