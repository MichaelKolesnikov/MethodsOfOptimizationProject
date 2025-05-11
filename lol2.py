import copy


def get_second_min(arr):
    assert len(arr) >= 2
    min1, min2 = float("inf"), float("inf")
    min1 = arr[0]
    if arr[1] < min1:
        min2 = min1
        min1 = arr[1]
    else:
        min2 = arr[1]
    for i in range(2, len(arr)):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]
    return min2

def get_min_for_rows(matrix):
    return {i: min(matrix[i].values()) for i in matrix}

def get_min_for_columns(matrix):
    n = len(matrix)
    min_ = {j: float("inf") for j in matrix[list(matrix.keys())[0]]}
    for i in matrix:
        for j in matrix[i]:
            min_[j] = min(min_[j], matrix[i][j])
    return min_

def get_row_reduced_matrix(matrix):
    min_ = get_min_for_rows(matrix)
    for i in matrix:
        for j in matrix[i]:
            matrix[i][j] -= min_[i]
    return matrix, sum(min_.values())

def get_column_reduced_matrix(matrix):
    min_ = get_min_for_columns(matrix)
    for i in matrix:
        for j in matrix[i]:
            matrix[i][j] -= min_[j]
    return matrix, sum(min_.values())

def get_reduced_matrix(matrix):
    m, h1 = get_row_reduced_matrix(matrix)
    m, h2 = get_column_reduced_matrix(m)
    return m, h1 + h2

def input_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def prepare_matrix_to_tsp_problem(matrix):
    n = len(matrix)
    return {
        i: {
            j:
                matrix[i][j] if i != j
                else float("inf")
            for j in range(n)
        }
        for i in range(n)
    }

def find_best_pair(matrix):
    q = -1
    cur = (-1, -1)
    for i in matrix:
        for j in matrix[i]:
            if matrix[i][j] == 0:
                cur_q = get_second_min(list(matrix[i].values())) + get_second_min([matrix[i_][j] for i_ in matrix])
                if cur_q > q:
                    q = cur_q
                    cur = (i, j)
    return cur, q

def cut_ij(matrix, i, j):
    del matrix[i]
    for i_ in matrix:
        del matrix[i_][j]
    if j in matrix and i in matrix[j]:
        matrix[j][i] = float("inf")
    return matrix

def solve(matrix, path, h_prev):
    if len(matrix) == 2:
        return path, h_prev
    m1 = copy.deepcopy(matrix)
    m1, h = get_reduced_matrix(m1)
    pair, q = find_best_pair(m1)
    path1, h1 = solve(cut_ij(copy.deepcopy(m1), *pair), path + [pair], h_prev + h)

    m2 = copy.deepcopy(copy.deepcopy(m1))
    m2[pair[0]][pair[1]] = float('inf')
    m2, h2 = get_reduced_matrix(m2)
    if h_prev + h + h2 < h1:
        return solve(m2, path, h_prev + h2)
    return path1, h1



def main():
    n = int(input())
    m = prepare_matrix_to_tsp_problem(input_matrix(n))
    path, h = solve(m, [], 0)
    print(path, h)



if __name__ == "__main__":
    main()
