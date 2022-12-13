# TODO здесь писать код


class Student:
    def __init__(self, name, number_groop, grades,  average_grades):
        self.name = name
        self.number_groop = number_groop
        self.grades_student = grades
        self.average_grades = average_grades

    def info_students(self):
        print('Фамилия Имя Отчество: {}\n'
              'Номер группы: {}\n'
              'Оценки: {}\n'
              'Средняя оценка: {}\n'.format(
            self.name, self.number_groop, self.grades_student, self.average_grades))


"""Оценки студента"""


def add_grades(grades):
    temp = []
    for i_grades in grades:
        temp.append(int(i_grades))
    return temp


"""средняя оценка студента"""


def average_grades(grades):
    average = sum(grades) / len(grades)
    return int(average)


text = open('info_students.txt', 'r', encoding='utf-8')
list_student = []
for string in text:
    for symbol in string.split():
        list_student.append(symbol)

new_list_student = []
while len(list_student) != 0:
    name_student = ' '.join(list_student[0:3])  # ФИО студента
    group_student = list_student[3]  # номер группы
    grades_student = add_grades(list_student[4:9])  # оценки
    average_grade_student = average_grades(grades_student)  # средняя оценка
    new_list_student.append([name_student, group_student, grades_student,
                             average_grade_student])

    del list_student[0:9]

sorted_list_student = (sorted(new_list_student, key=lambda x: x[-1], reverse=True))

for i_index in range(len(sorted_list_student)):
    name = sorted_list_student[i_index][0]
    group = sorted_list_student[i_index][1]
    grades = sorted_list_student[i_index][2]
    average_grade = sorted_list_student[i_index][3]
    student = Student(name, group, grades, average_grade)
    student.info_students()


