# TODO здесь писать код
class Circle:

    def __init__(self, name, x, y, r):
        self.name = name
        self.x = x
        self.y = y
        self.r = r

    def print(self):
        print('Name: {}\n'
              'Центр круга:\n'
              'X: {}\n'
              'Y: {}\n'
              'R: {}\n'.format(self.name, self.x, self.y, self.r))

    """Вычисление занимаемых координат"""

    def circle_board(self):
        self.x_1 = self.x + self.r
        self.x_2 = self.x - self.r
        self.y_1 = self.y + self.r
        self.y_2 = self.y - self.r

    def print_R(self):
        print('Занимаемые координаты:\n'
              'X_1: {}\n'
              'X_2: {}\n'
              'Y_1: {}\n'
              'Y_2: {}\n'.format(self.x_1, self.x_2, self.y_1, self.y_2))

    def check_circles(self):
        pass


circle_1 = Circle('Круг-1', 0, 0, 1)
circle_1.circle_board()
circle_1.print()
circle_1.print_R()

circle_2 = Circle('Круг-2', 2, 2, 4)
circle_2.circle_board()
circle_2.print()
circle_2.print_R()
