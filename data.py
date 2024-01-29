import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


data = {
    22: 150,
    23: 155,
    24: 160,
    25: 162,
    26: 171,
    27: 174,
    28: 180,
    29: 183,
    30: 189,
    31: 192
}
point_list = [Point(key, value) for key, value in data.items()]


def Linear(data):
    summa_x = 0
    summa_y = 0
    summa_x_2 = 0
    summa_x_y = 0
    n = len(data)

    for i in range(n):
        summa_x += float(data[i].x)
        summa_y += float(data[i].y)
        summa_x_2 += float(data[i].x) * float(data[i].x)
        summa_x_y += float(data[i].x) * float(data[i].y)

    matrix = np.array([[n, summa_x], [summa_x, summa_x_2]])
    vector = np.array([summa_y, summa_x_y])
    out = np.linalg.solve(matrix, vector)

    a = float(out[0])
    b = float(out[1])
    return [a, b]


def show(data, a, b):
    n = len(data)
    min = data[0].x
    max = data[0].x
    first = 0
    end = 0

    for i in range(n):
        if data[i].x < min:
            min = data[i].x
            first = i
        if data[i].x > max:
            max = data[i].x
            end = i

    linex = [data[first].x, data[end].x]
    liney = [a + b * data[first].x, a + b * data[end].x]

    x = []
    y = []

    for i in range(n):
        x.append(data[i].x)
        y.append(data[i].y)

    line1 = plt.scatter(x, y, c='pink', s=30, alpha=0.9, edgecolors='black',
                        label='Data')  # Отрисовка точек
    line2 = plt.plot(linex, liney, linestyle='--', label='Fitted')  #

    fig = plt.gcf()

    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend(loc=0)

    plt.show()


k = Linear(point_list)  # Вычисление коэффициентов
show(point_list, k[0], k[1])  # Отображение
