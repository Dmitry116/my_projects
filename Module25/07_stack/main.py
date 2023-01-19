# TODO здесь писать код
class TaskManager:

    def __init__(self):
        self.dict_task = {}

    def new_task(self, key, value):
        """Добавление задачи с преоритетом в словарь"""
        if value in self.dict_task:
            self.dict_task[value] += [key]
        else:
            self.dict_task[value] = [key]

    def sort_dict(self):
        """Сортирует ключи self.dict_task"""
        sort_key = sorted(self.dict_task)
        return sort_key

    def get_dict_task(self):
        return self.dict_task

    def show_tasks(self):
        #tasks = self.get_dict_task()
        for key in self.sort_dict():
            print(f'{key} {"; ".join(self.dict_task[key])}')


class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        """Отправляет значение словаря в список"""
        self.list.append(value)

    def get_stack(self):
        """Удяляет последний элемент стека"""
        if len(self.list) == 0:
            pass
        else:
            return self.list.pop()

    def isempty(self):
        """Проверка пустой стек или нет"""
        return len(self.list) == 0

    def get_list(self):
        return self.list


manager = TaskManager()
new_stack = Stack()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

manager.show_tasks()

for key, value in sorted(manager.get_dict_task().items()):
    new_stack.push(value)
print('Стек пуст:', new_stack.isempty())

for _ in range(len(new_stack.get_list())):
    new_stack.get_stack()
print('Стек пуст:', new_stack.isempty())

