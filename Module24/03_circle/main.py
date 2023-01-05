import math


class Circle:
    pi = 3.14159

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area_circle(self):
        """"Площадь круга"""
        return self.pi * self.r ** 2

    def long_circumference(self):
        """Длинна окружности"""
        return 2 * self.pi * self.r

    def radius_increase(self, num):
        """Увеличение длинны окружности"""
        self.r *= num

    def is_intersect(self, other_circle):
        if self.x == other_circle.x and self.y == other_circle.y:
            print('окружности совпадают')
            return self.r == other_circle.r

        centers_distance = math.sqrt(
            (self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2)
        if self.r + other_circle.r - centers_distance < (self.r + other_circle.r) ** 2:
            if abs(self.r - other_circle.r) - centers_distance < (self.r + other_circle.r) ** 2:
                print('радиусы не совпадают')
                return True
        return False


circle_1 = Circle(0, 1, 2)
circle_2 = Circle(0, 0, 1)

print(circle_1.is_intersect(circle_2))
