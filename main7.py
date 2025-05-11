import numpy as np
import math


def reduce_matrix(matrix):
    """Reduce a cost matrix by subtracting the smallest value in each row and column."""
    row_min = np.min(matrix, axis=1)
    row_min[row_min == math.inf] = 0
    matrix = matrix - row_min[:, None]

    col_min = np.min(matrix, axis=0)
    col_min[col_min == math.inf] = 0
    matrix = matrix - col_min

    return matrix, row_min.sum() + col_min.sum()


def calculate_penalties(matrix):
    """Calculate penalties for assigning each zero in the cost matrix."""
    penalties = np.zeros_like(matrix)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 0:
                row_values = np.delete(matrix[i, :], j)
                col_values = np.delete(matrix[:, j], i)

                row_penalty = np.min(row_values) if row_values.size > 0 else 0
                col_penalty = np.min(col_values) if col_values.size > 0 else 0

                penalties[i, j] = row_penalty + col_penalty

    return penalties


def tsp_little_algorithm(cost_matrix):
    """Solve the Traveling Salesman Problem using Little's algorithm."""
    n = cost_matrix.shape[0]
    best_cost = math.inf
    best_path = []

    matrix = cost_matrix.copy()
    total_cost = 0
    path = []

    while len(path) < n:
        matrix, reduction_cost = reduce_matrix(matrix)
        total_cost += reduction_cost

        penalties = calculate_penalties(matrix)
        max_penalty_index = np.unravel_index(np.argmax(penalties, axis=None), penalties.shape)

        i, j = max_penalty_index
        path.append((i, j))

        # Block row i and column j and prevent returning to node i
        matrix[i, :] = math.inf
        matrix[:, j] = math.inf
        matrix[j, i] = math.inf

    # Reconstruct the path in order
    path.sort()
    ordered_path = [path[0][0]]
    for _ in range(len(path)):
        for start, end in path:
            if start == ordered_path[-1]:
                ordered_path.append(end)
                break

    return total_cost, ordered_path


# Test the algorithm
cost_matrix = np.array([
    [math.inf, 20, 30, 10, 11],
    [15, math.inf, 16, 4, 2],
    [3, 5, math.inf, 2, 4],
    [19, 6, 18, math.inf, 3],
    [16, 4, 7, 16, math.inf]
])

total_cost, ordered_path = tsp_little_algorithm(cost_matrix)
