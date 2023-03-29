import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from matplotlib import animation

def runtime():
    print("1.сравнение скорости стандартного умножения и умножения с помощью библиотеки numpy")
    #стандартное умножение
    case_one_start_time = time.perf_counter()
    random_list_one = []
    random_list_two = []

    for i in range(1000000):
        random_list_one.append(round(random.random()*10, 0))
        random_list_two.append(round(random.random()*10, 0))
    multiplied = [a * b for a, b in zip(random_list_one, random_list_two)]

    case_one_end_time = time.perf_counter()
    case_one_time = case_one_end_time-case_one_start_time

    print(f'время, затраченное на стандартное умножение: {case_one_time}')

    #умножение numpy
    case_two_start_time = time.perf_counter()

    random_list_one = np.random.randint(0,100,(1, 1),dtype='int64')
    random_list_two = np.random.randint(0,100,(1, 1000000),dtype='int64')
    multiplied = np.multiply(random_list_one, random_list_two)

    case_two_end_time = time.perf_counter()
    case_two_time = case_two_end_time-case_two_start_time

    print(f'время, затраченное на умножение numpy: {case_two_time}')

def graph():
    print("2. Операции с csv-файлами и построение графика")
    arr = np.genfromtxt('data1.csv', delimiter=';')
    x = arr[:, 1]
    y1 = arr[:, 4]
    y2 = arr[:, 18]

    #superimposed graph
    fig, ax = plt.subplots()
    ax.plot(x, y1, color='blue', label='Graph 1')
    ax.plot(x, y2, color='red', label='Graph 2')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('График')
    ax.legend()
    plt.show()

    #correlation graph
    corr = np.corrcoef(y1, y2)[0, 1]
    plt.scatter(y1, y2)
    plt.title("график корреляции y1 и y2")
    plt.xlabel("y1")
    plt.ylabel("y2")
    plt.legend(["Data"])
    plt.plot([min(y1), max(y1)], [min(y2), max(y2)], 'r--')
    plt.show()

def plot3d():
    print('3. Построение 3d-графика x, y и z.')
    x = np.linspace(-5*np.pi, 5*np.pi)
    y = np.cos(x)
    z = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, c='blue')
    plt.show()

def animate_func():
    fig, ax = plt.subplots()

    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)
    line, = plt.plot(x, y)

    def animated(i):
        line.set_ydata(np.sin(x + i / 30))
        return line,

    anim = animation.FuncAnimation(fig, animated, interval=10, blit=True, save_count=20)

    plt.show()


#upload the csv file data1.csv
if __name__ == "__main__":
    runtime()
    graph()
    plot3d()
    animate_func()
