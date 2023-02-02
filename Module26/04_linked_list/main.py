# TODO здесь писать код
class Node():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, data):

        """Добавления значений"""

        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def get(self, index):

        """Получение элемента по индексу"""

        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print('индекс вне диапазона')

    def remove(self, index):

        """Удаление элемента по индексу"""

        cur_node = self.head
        count = 0
        while cur_node != None:
            if index == 0:
                self.head = cur_node.get_next()
                return
            elif count + 1 == index:
                remove_data = cur_node.get_next()
                after_data = remove_data.get_next()
                cur_node.set_next(after_data)
                return

    def print_list(self):

        """Выводит список элементов"""

        cur_node = self.head
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data()) + ' '
            cur_node = cur_node.get_next()
        return output


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print('Текущий список:', my_list.print_list())
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list.print_list())
