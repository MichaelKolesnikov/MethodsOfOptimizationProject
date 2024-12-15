import random
from functions import *

def get_second_min(arr):
    assert len(arr) >= 2
    min1, min2 = float("inf"), float("inf")
    min1 = arr[0]
    if arr[1] < min1:
        min2 = min1
        min1 = arr[1]
    for i in range(2, len(arr)):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]
    return min2

def get_min_for_rows_in_c(matrix):
    return {i: get_second_min(list(matrix[i].values())) for i in matrix}
def get_min_for_columns_in_c(matrix):
    columns = {}
    min_ = {}
    for i in matrix:
        for j in matrix[i]:
            if j not in columns:
                columns[j] = []
            columns[j].append(matrix[i][j])
    min_ = {i: get_second_min(columns[i]) for i in columns}
    return min_

def get_row_reduced_c(matrix):
    _matrix = copy.deepcopy(matrix)
    min_ = get_min_for_rows_in_c(matrix)
    for i in matrix:
        for j in matrix[i]:
            _matrix[i][j] -= min_[i]
    return _matrix
def get_column_reduced_c(matrix):
    _matrix = copy.deepcopy(matrix)
    min_ = get_min_for_columns_in_c(matrix)
    for i in matrix:
        for j in matrix[i]:
            _matrix[i][j] -= min_[j]
    return _matrix
def get_reduced_c(matrix):
    return get_column_reduced_c(get_row_reduced_c(matrix))

def only_0_and_inf(matrix):
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] not in [0, float("inf")]:
                return False
    return True


def solve_tsp(matrix):
    n = len(matrix)
    c = copy.deepcopy(matrix)
    cost = float('inf')
    path = []
    phi = sum(get_min_for_rows(c) + get_min_for_columns(c))
    print(phi)
    c = get_r_c_reduced_matrix(c)
    print("Редуцированная матрица:")
    print_matrix(c)
    c = {i: {j: c[i][j] for j in range(n)} for i in range(n)}
    print("Минимумы:")
    print_c_with(c)
    while not only_0_and_inf(c):
        row_min = get_min_for_rows_in_c(c)
        column_min = get_min_for_columns_in_c(c)
        max_sum = -1
        row_index, column_index = 0, 0
        for i in c:
            for j in c[i]:
                if c[i][j] != 0:
                    continue
                cur = row_min[i] + column_min[j]
                print(i, j, cur)
                if cur > max_sum:
                    max_sum = cur
                    row_index, column_index = i, j
        print("Максимальный коэффициент", row_index, column_index, max_sum)
        del c[row_index]
        for i in c:
            del c[i][column_index]
        if column_index in c and row_index in c[column_index]:
            c[column_index][row_index] = float("inf")
        print("Удаляем строку и столбец, делаем противоположный элемент бесконечным")
        print_c_with(c)
        c = get_reduced_c(c)
        print("Редуцированная матрица:")
        print_c_with(c)
        input()



    return cost, path


def generate_random_matrix(n, max_weight=100):
    matrix = [[random.randint(1, max_weight) if i != j else float("inf") for j in range(n)] for i in range(n)]
    return matrix


def print_c_with(matrix):
    print("|  | ", end='')
    for i in matrix:
        print(*matrix[i], sep=' | ', end='')
        break
    print("| min |")
    row_min = get_min_for_rows_in_c(matrix)
    for i in matrix:
        print(f"|{i} | ", end='')
        for j in matrix[i]:
            print(matrix[i][j], end=' | ')
        print(f"{row_min[i]} |")
    print("| min | ", end='')
    print(*get_min_for_columns_in_c(matrix).values(), sep=" | ", end='')
    print(" | |")
    print()

def main():
    n = int(input("Введите размер матрицы (n): "))
    print("Выберите опцию:")
    print("1. Ввести свою матрицу")
    print("2. Сгенерировать случайную матрицу")
    option = int(input("Ваш выбор (1 или 2): "))

    if option == 1:
        matrix = input_matrix(n)
        for i in range(n):
            matrix[i][i] = float("inf")
    elif option == 2:
        matrix = generate_random_matrix(n)
        print("Сгенерированная матрица:")
        print_matrix(matrix)
    else:
        print("Некорректный выбор.")
        return

    cost, path = solve_tsp(matrix)
    print("\nМинимальная стоимость:", cost)
    print("Оптимальный путь:", " -> ".join(map(str, path)))


if __name__ == "__main__":
    main()
