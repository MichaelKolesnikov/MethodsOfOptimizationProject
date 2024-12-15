import copy


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
def print_markdown_matrix(matrix):
    m = len(matrix[0])
    print("| " * (m + 1))
    print("| --- " * m + "|")
    for i in range(len(matrix)):
        print(f"| ", end='')
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' | ')
        print()


def input_matrix(n):
    print(f"Введите матрицу размера {n} x {n} (через пробелы, элементы разделяются строками):")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def get_min_for_rows(matrix):
    return [min(i) for i in matrix]


def get_min_for_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if m != len(matrix[i]):
            raise "It is not matrix"
    min_ = [float("inf")] * m
    for i in range(n):
        for j in range(m):
            min_[j] = min(min_[j], matrix[i][j])
    return min_


def get_row_reduced_matrix(matrix):
    _matrix = copy.deepcopy(matrix)
    min_ = get_min_for_rows(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            _matrix[i][j] -= min_[i]
    return _matrix


def get_column_reduced_matrix(matrix):
    _matrix = copy.deepcopy(matrix)
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if m != len(matrix[i]):
            raise "It is not matrix"
    min_ = get_min_for_columns(matrix)
    for i in range(n):
        for j in range(m):
            _matrix[i][j] -= min_[j]
    return _matrix


def get_r_c_reduced_matrix(matrix):
    return get_column_reduced_matrix(get_row_reduced_matrix(matrix))


def get_c_r_reduced_matrix(matrix):
    return get_row_reduced_matrix(get_column_reduced_matrix(matrix))
