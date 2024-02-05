import math

class Vector:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def getCoords(self):
         return self.__x, self.__y, self.__z

    # сложение
    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    # вычитание
    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)


    # обратный вектор
    def inverse(self):
        return Vector(-self.__x, -self.__y, -self.__z)

    # скалярное произведение 2х векторов
    def scalar_p(self, other):
        return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z

    # векторное произведение
    def vector_p(self, other):
        x = self.__y * other.__z - self.__z * other.__y
        y = self.__z * other.__x - self.__x * other.__z
        z = self.__x * other.__y - self.__y * other.__x
        return Vector(x, y, z)

    # смешанное произведение
    def mixed_p(self, b, c):
        return self.scalar_p(b.vector_p(c))

    # длина
    def range(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    # единичный вектор
    def norm(self):
        return Vector(self.__x / self.range(), self.__y / self.range(), self.__z / self.range())

    # угол между векторами
    def angle(self, other):
        cos = self.scalar_p(other) / (self.range() * other.range())
        return math.acos(cos)

    # коллинеарность
    def check_collinear(self, other):
        return self.vector_p(other).range() == 0

    # Проверка на компланарность - смешанное произведение = 0
    def check_coplanar(self, b, c):
        return self.mixed_p(b, c) == 0


def parse_input(input_str):
    mas = input_str.split(',')
    return float(mas[0]), float(mas[1]), float(mas[2])


def main():
    while True:
        print('1 - Сложение\n'
              '2 - Вычитание\n'
              '3 - Скалярное произведение\n'
              '4 - Векторное произведение\n'
              '5 - Коллинеарность\n'
              '6 - Компланарность\n'
              '7 - Угол между векторами\n'
              '8 - Выход')
        choice = input('Номер операции - ')

        if choice == '8':
            break

        if choice in ['1', '2', '3', '4', '5', '7']:
            vec1_input = input('Координаты 1-го вектора  (x,y,z): ')
            x, y, z = parse_input(vec1_input)
            vec1 = Vector(x, y, z)
            vec2_input = input('Координаты 2-го вектора  (x,y,z): ')
            x, y, z = parse_input(vec2_input)
            vec2 = Vector(x, y, z)



        if choice == '1':
            result = vec1.__add__(vec2)
            print(f'Результат: {result.getCoords()}')
        elif choice == '2':
            result = vec1.__sub__(vec2)
            print(f'Результат: {result.getCoords()}')
        elif choice == '3':
            result = vec1.scalar_p(vec2)
            print(f'Результат: {result}')
        elif choice == '4':
            result = vec1.vector_p(vec2)
            print(f'Результат: {result.getCoords()}')
        elif choice == '5':
            result = vec1.check_collinear(vec2)
            print(f'Результат: {result}')
        elif choice == '7':
            angle = vec1.angle(vec2)
            print(f'Результат: {math.degrees(angle)} градусов')
        elif choice == '6':
            vec1_input = input('Координаты 1-го вектора  (x,y,z): ')
            x, y, z = parse_input(vec1_input)
            vec1 = Vector(x, y, z)
            vec2_input = input('Координаты 2-го вектора  (x,y,z): ')
            x, y, z = parse_input(vec2_input)
            vec2 = Vector(x, y, z)
            vec3_input = input('Координаты 3-го вектора (x,y,z): ')
            x, y, z = parse_input(vec3_input)
            vec3 = Vector(x, y, z)
            result = vec1.check_coplanar(vec2, vec3)
            print(f'Результат: {result}')


if __name__ == '__main__':
    main()