# TODO здесь писать код

def rename_female(name):
    female_list = []
    name = name.replace(key, value)
    for i_name in family:
        if name in i_name:
            female_list.append(i_name)
    return female_list

def rename_male(name):
    male_list = []
    name = name.replace(value, key)
    for i_name in family:
        if name in i_name:
            male_list.append(i_name)
    return male_list

family = {
('Сидоров', 'Никита'): 35,
('Антонова', 'Екатерина'): 17,
('Сидорова', 'Алина'): 34,
('Сидоров', 'Павел'): 10,
('Антонов', 'Павел'): 20
}

name = input('Введите фамилию: ').title()
ending_dict = {
        'ов': 'ова',
        'ев': 'ева',
        'ий': 'ая'
}

for i_name in family:
    if name in i_name:
        print(*i_name, family[i_name])


for key, value in ending_dict.items():
    if name.endswith(key):
        rename_female(name)
        for i_rename_female in rename_female(name):
            print(*i_rename_female, family[i_rename_female])
    elif name.endswith(value):
        rename_male(name)
        for i_rename_male in rename_male(name):
            print(*i_rename_male, family[i_rename_male])