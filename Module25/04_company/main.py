# TODO здесь писать код
class Person:
    def __init__(self, first_name, second_name, age):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age

    def get_first_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, first_name, second_name, age, salary):
        super().__init__(first_name, second_name, age)
        self.salary = salary

    def print_info(self):
        print('Имя: {}\n'
              'Фамилия: {}\n'
              'Возраст: {}\n'
              'Зарплата: {}\n'.format(self.get_first_name(), self.get_second_name(), self.get_age(), self.salary))


class Manager(Employee):
    def __init__(self, first_name, second_name, age, salary):
        super().__init__(first_name, second_name, age, salary)


class Agent(Employee):
    def __init__(self, first_name, second_name, age, salary, sales):
        super().__init__(first_name, second_name, age, salary)

        self.salary = salary + (sales - (sales - sales / 100 * 5))


class Worker(Employee):
    def __init__(self, first_name, second_name, age, salary, hours):
        super().__init__(first_name, second_name, age, salary)

        self.salary = salary * hours


manager_1 = Manager('Tom', 'Soyer', 36, 13000)
manager_2 = Manager('Benicio', 'Del Toro', 55, 13000)
manager_3 = Manager('Anna', 'Tomson', 28, 13000)
manager_1.print_info()
manager_2.print_info()
manager_3.print_info()

agent_1 = Agent('Mett', 'Greiver', 54, 100, 20000)
agent_2 = Agent('Emilio', 'Santos', 32, 5000, 10000)
agent_3 = Agent('Lao', 'Si', 27, 5000, 15000)
agent_1.print_info()
agent_2.print_info()
agent_3.print_info()

worker_1 = Worker('Jon', 'Bernthal', 55, 100, 160)
worker_2 = Worker('Hulio', 'Sedilio', 53, 100, 155)
worker_3 = Worker('Raul', 'Truhilio', 67, 100, 158)
worker_1.print_info()
worker_2.print_info()
worker_3.print_info()
