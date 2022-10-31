# TODO здесь писать код
import random

def random_numbers():
    return  [random.randint(0, 10) for _ in range(10)]


def separe_numbers(random_numbers):
    num_list_1 = [random_numbers[i] for i in range(len(random_numbers)) if not i % 2]
    num_list_2 = [random_numbers[i] for i in range(len(random_numbers)) if i % 2]
    return num_list_1, num_list_2


def zip_numbers(num_list_1, num_list_2):
    zip_num = [(num_list_1[i_elem], num_list_2[i_elem]) for i_elem in range(min(len(num_list_1), len(num_list_2)))]
    return zip_num


def display(zip_numbers):
    print(random_numbers)
    print(list(zip_numbers))


random_numbers = random_numbers()
num_list_1, num_list_2 = separe_numbers(random_numbers)
total_list = zip_numbers(num_list_1, num_list_2)
display(total_list)