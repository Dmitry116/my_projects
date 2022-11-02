num_fact = {}
while True:

    def calculating_math_func(data, num_fact=None):
        result = 1
        if data in num_fact:
            result = num_fact[data]

        else:
            for index in range(1, data + 1):
                result *= index
        num_fact[data] = (result)
        result /= data ** 3
        result = result ** 10
        return result


    num = int(input('Введите число: '))
    print(calculating_math_func(num, num_fact))
    print(num_fact)
