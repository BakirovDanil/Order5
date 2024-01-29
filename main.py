import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:
    def __init__(self, data):
        self.data = data
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):
        n = len(self.data)

        x_values = np.array([point.x for point in self.data])
        y_values = np.array([point.y for point in self.data])

        summa_x = np.sum(x_values)
        summa_y = np.sum(y_values)
        summa_x_2 = np.sum(x_values ** 2)
        summa_x_y = np.sum(x_values * y_values)

        matrix = np.array([[n, summa_x], [summa_x, summa_x_2]])
        vector = np.array([summa_y, summa_x_y])
        coefficients = np.linalg.solve(matrix, vector)

        return coefficients

    def show_plot(self):
        min_x = min(point.x for point in self.data)
        max_x = max(point.x for point in self.data)
        line_x = [min_x, max_x]
        line_y = [self.coefficients[0] + self.coefficients[1] * min_x,
                  self.coefficients[0] + self.coefficients[1] * max_x]

        x = [point.x for point in self.data]
        y = [point.y for point in self.data]

        plt.scatter(x, y, c='pink', s=30, alpha=0.9, edgecolors='black', label='Data')
        plt.plot(line_x, line_y, linestyle='--', label='Fitted')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc=0)
        plt.show()


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

# Использование класса LinearRegression
linear_regression = LinearRegression(point_list)
linear_regression.show_plot()
