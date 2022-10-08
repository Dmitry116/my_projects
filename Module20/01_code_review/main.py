students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def id_age(students):
    id_num = []
    ages = []

    for i_id, i_info in students.items():
        for _, i_age in i_info.items():
            if i_info['age'] == i_age:
                id_num.append(i_id)
                ages.append(i_age)
    id_num_students = zip(id_num, ages)

    return id_num_students


def interests(students):
    interests_list = []
    for i_id, i_info in students.items():
        for _, i_intersts in i_info.items():
            if i_info['interests'] == i_intersts:
                interests_list.extend(i_intersts)
    return interests_list


def len_surname(students):
    len_sur = ''.join([
                i_surname
                for i_id, i_info in students.items()
                    for _, i_surname in i_info.items()
                        if i_info['surname'] == i_surname
    ])
    return len_sur


def display_result(id_num_students, interests_list, len_sur):
    print('Список пар "ID студента — возраст": ', list(id_num_students))
    print('Полный список интересов всех студентов: ', interests_list)
    print('Общая длина всех фамилий студентов: ', len(len_sur))


id_age_students = id_age(students)
interests_student = interests(students)
len_surnames_students = len_surname(students)
display_result(id_age_students, interests_student, len_surnames_students)


# TODO исправить код
