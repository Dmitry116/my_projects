# TODO здесь писать код
class Student:
    def __init__(self,student_id, name, number_groop, grades):
        self.student_id = student_id
        self.name = name
        self.number_groop = number_groop
        self.grades = grades

    def info_students(self):
        print('Id номер студента: {}\n'
              'Фамилия Имя: {}\n'
              'Номер группы: {}\n'
              'Оценки: {}'.format(self.student_id, self.name, self.number_groop, self.grades))



for student_id in range(1, 2):
    try:
        name = input('Введите имя и фамилию: ').split()
        if len(name) < 2:
            raise NameError
    except:
        NameError('Не правильно записано имя и фамилия')
    number_groop = int(input('Введите номер группы: '))
    grades = []
    for i_num in range(5):
        grades_num = input(f'Введие {i_num+1}-ю оценку: ').split()
        grades.append(grades_num)
    student_id = Student(student_id, name, number_groop, grades)
    student_id.info_students()