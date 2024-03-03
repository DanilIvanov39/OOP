class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.__dim0 = dim0   #ширина
        self.__dim1 = dim1   #высота
        self.__dim2 = dim2   #глубина
        self.length = dim0*dim1*dim2
        self.arr = [0]*self.length

    def __str__(self):  # Преобразовываем написание массива
        result = ""
        for i in range(self.__dim0):
            result += f"Глубина: {i}\n"
            for j in range(self.__dim1):
                for k in range(self.__dim2):
                    result += f"{self.arr[self.transform_index(i, j, k)]} "
                result += "\n"
            result += "\n"
        return result

    def __getitem__(self, idx):
        i, j, k = idx
        return self.arr[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k]

    def __setitem__(self, idx, value):
        i, j, k = idx
        self.arr[i * self.__dim1 * self.__dim2 + j * self.__dim2 + k] = value

    def transform_index(self, i, j, k):
        return i + self.__dim0 * (j + self.__dim1 * k)  #перевод индекса

    def get_values0(self, i):  # Получаем срез по первому приближению = двумерный массив
        result = ""
        for j in range(self.__dim1):
            result += "\n"
            for k in range(self.__dim2):
                result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def get_values1(self, j):  # Получаем срез по первому приближению = двумерный массив
        result = ""
        for i in range(self.__dim0):
            result += "\n"
            for k in range(self.__dim2):
                result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def get_values2(self, k):  # Получаем срез по первому приближению = двумерный массив
        result = ""
        for i in range(self.__dim0):
            result += "\n"
            for j in range(self.__dim1):
                result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def get_values01(self, i, j):  # Получаем срез по второму приближению = одномерный массив
        result = ""
        for k in range(self.__dim2):
            result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def get_values02(self, i, k):  # Получаем срез по второму приближению = одномерный массив
        result = ""
        for j in range(self.__dim1):
            result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def get_values12(self, j, k):  # Получаем срез по второму приближению = одномерный массив
        result = ""
        for i in range(self.__dim0):
            result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def set_values0(self, i, array):  # Устанавливаем значение в массиве для заданной одной координаты (ставим необходимый двумерный массив)
        for k in range(self.__dim2):
            for j in range(self.__dim1):
                self.arr[self.transform_index(i, j, k)] = array[k][j]
        return self.arr

    def set_values1(self, j, array):  # Устанавливаем значение в массиве для заданной одной координаты (ставим необходимый двумерный массив)
        for i in range(self.__dim0):
            for k in range(self.__dim2):
                self.arr[self.transform_index(i, j, k)] = array[k][j]
        return self.arr

    def set_values2(self, k, array):  # Устанавливаем значение в массиве для заданной одной координаты (ставим необходимый двумерный массив)
        for i in range(self.__dim0):
            for j in range(self.__dim1):
                self.arr[self.transform_index(i, j, k)] = array[k][j]
        return self.arr

    def set_values01(self, i, j, array):  # Устанавливаем значение в массиве для заданных двух координат (ставим необходимый одномерный массив)
        for k in range(self.__dim2):
            self.arr[self.transform_index(i, j, k)] = array[k]
        return self.arr

    def set_values02(self, i, k, array):  # Устанавливаем значение в массиве для заданных двух координат (ставим необходимый одномерный массив)
        for j in range(self.__dim1):
            self.arr[self.transform_index(i, j, k)] = array[k]
        return self.arr

    def set_values12(self, j, k, array):  # Устанавливаем значение в массиве для заданных двух координат (ставим необходимый одномерный массив)
        for i in range(self.__dim0):
            self.arr[self.transform_index(i, j, k)] = array[k]
        return self.arr

        # cоздает массив заполненный 1
    def np_ones(self):
            self.arr = [1] * self.length

        # cоздает массив заполненный 0
    def np_zeros(self):
            self.arr = [0] * self.length

        # cоздает массив заполненный определенным числом
    def np_fill(self, value):
            self.arr = [value] * self.length



if __name__ == '__main__':
    array = Array3d(3, 3, 3)
    array.set_values0(0, [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    array.set_values0(1, [[4, 5, 6], [4, 5, 6], [4, 5, 6]])
    array.set_values0(2, [[7, 8, 9], [7, 8, 9], [7, 8, 9]])

    print(array.get_values01(0, 2))
    print(array)
    print(array[1, 0, 1])
    print(array[0, 0, 0])
    array[0, 0, 0] = 7
    print(array[0, 0, 0])
