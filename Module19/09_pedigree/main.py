# TODO здесь писать код

def get_input_parameters():
    people = int(input('Введите количество человек: '))
    return people


def separ_name(people):
    name_dict = {}
    level_dict = {}
    for i in range(1, people):
        pair_man = input(f'{i}-я пара: ')
        child, parent = pair_man.split()
        name_dict[child] = parent
        level_dict[child] = 0
        level_dict[parent] = 0
    return name_dict, level_dict


def level_names(name_dict, level_dict):
    for i in name_dict:
        people = i
        while people in name_dict:
            people = name_dict[people]
            level_dict[i] += 1
    return level_dict


def display_result(level):
    for name_lvl in sorted(level_dict):
        print(name_lvl, level_dict[name_lvl])


people = get_input_parameters()
name_dict, level_dict = separ_name(people)
level = level_names(name_dict, level_dict)
display_result(level)


