import matplotlib.pyplot as plt
import numpy as np


def plot_vector_and_lines(a, b, lines):
    plt.figure(figsize=(8, 6))

    plt.quiver(0, 0, a, b, angles='xy', scale_units='xy', scale=1, color='r', label='grad(F)')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    colors = ['b', 'g', 'm', 'c', 'y', 'k', 'orange', 'purple', 'brown', 'pink']

    # Рисуем прямые
    x_vals = np.linspace(-10, 10, 400)
    for i, (k1, k2, bi) in enumerate(lines):
        if k2 == 0:  # Вертикальная прямая
            x_val = bi / k1
            plt.axvline(x_val, color=colors[i % len(colors)], label=f'x = {x_val}')
        elif k1 == 0:  # Горизонтальная прямая
            y_val = bi / k2
            plt.axhline(y_val, color=colors[i % len(colors)], label=f'y = {y_val}')
        else:  # Обычная прямая
            y_vals = (bi - k1 * x_vals) / k2
            plt.plot(x_vals, y_vals, color=colors[i % len(colors)], label=f'{k1}x + {k2}y = {bi}')

    plt.xticks(np.arange(-5, 5, 1))
    plt.yticks(np.arange(-50, 5, 1))
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.legend()
    plt.title('Vector and Lines')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


with open("Work6/a.txt") as f:
    a, b = map(int, f.readline().split())
    n = int(f.readline())
    lines = []
    for i in range(n):
        lines.append(list(map(int, f.readline().split())))


plot_vector_and_lines(a, b, lines)
