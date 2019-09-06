# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt

class Triangle:
    def __init__(self, A1, A2, A3):
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3

    def area(self):
        return 0.5*((self.A2[0] - self.A1[0])*(self.A3[1] - self.A1[1]) - (self.A3[0] - self.A1[0])*(self.A2[1] - self.A1[1]))

    def height(self):
        P = self.perimeter()/2
        a = (2 * sqrt(P*(P-self.AB)*(P-self.AC)*(P-self.BC)))/self.AB
        b = (2 * sqrt(P*(P-self.AB)*(P-self.AC)*(P-self.BC)))/self.BC
        c = (2 * sqrt(P*(P-self.AB)*(P-self.AC)*(P-self.BC)))/self.AC

        return f'Высота от стороны  A={a};B={b};C={c} '

    def perimeter(self):
        self.AB = round(sqrt((self.A2[0] - self.A1[0])**2 + (self.A2[1] - self.A1[1])**2))
        self.AC = round(sqrt((self.A3[0] - self.A1[0])**2 + (self.A3[1] - self.A1[1])**2))
        self.BC = round(sqrt((self.A3[0] - self.A2[0])**2 + (self.A3[1] - self.A2[1])**2))

        #print(f'Длины сторон AB={self.AB}; BC={self.BC}; AC={self.AC}')

        return self.AB + self.AC + self.BC

new = Triangle([5, 2], [7, 3], [5, 7])
print(f' Площадь', new.area())
print(f' Периметр', new.perimeter())
print(new.height())
print('=================')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
class Trapezia:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = round(sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2))
        self.BC = round(sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2))
        self.CD = round(sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[1]) ** 2))
        self.AD = round(sqrt((self.D[0] - self.A[0]) ** 2 + (self.D[1] - self.A[1]) ** 2))

        # Равнобедренная трапеция – трапеция, у которой боковые стороны равны.
        if self.AB != self.CD:
            print(f'Трапеция не равнобедренная!\n Сторона AB={self.AB} не равна CD={self.CD}')
        else:
            print(f'Трапеция равнобедренная!\n Сторона AB={self.AB} равна CD={self.CD}')

    # длины сторон
    def length(self):
        return f'Длины сторон AB={self.AB}; BC={self.BC}; CD={self.CD}; AD={self.AD}'

    def perimeter(self):
        return  self.AB + self.BC + self.CD + self.AD

    def area(self):
        return 0.5*(self.BC-self.AD/2)*(self.BC+self.AD)

# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

trap = Trapezia([3,2], [5,2], [8,6], [6,6])
print(trap.length())
print('Периметр',trap.perimeter())
print('Площадь',trap.area())