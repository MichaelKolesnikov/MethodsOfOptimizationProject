from random import randint

import numpy as np
from scipy.optimize import linear_sum_assignment


def hungarian_algorithm(cost_matrix):
    cost_matrix = np.array(cost_matrix)

    # Check if the matrix is rectangular and non-empty
    if len(cost_matrix.shape) != 2 or cost_matrix.shape[0] == 0 or cost_matrix.shape[1] == 0:
        raise ValueError("Cost matrix must be a non-empty 2D array.")

    row_indices, col_indices = linear_sum_assignment(cost_matrix)

    return row_indices.tolist(), col_indices.tolist()


def main():
    try:
        n = int(input())
        should_be_generated = input("Write something to generate table")
        if should_be_generated:
            cost_matrix = [[randint(1, 9) for j in range(n)] for _ in range(n)]
            for i in cost_matrix:
                print(*i)
        else:
            cost_matrix = [list(map(int, input().split())) for _ in range(n)]
        row_ind, col_ind = hungarian_algorithm(cost_matrix)
        print("Optimal assignment:")
        optimal_assignment = [[0 for j in range(n)] for i in range(n)]
        for r, c in zip(row_ind, col_ind):
            optimal_assignment[r][c] = 1
        for i in optimal_assignment:
            print(*i)

        total_cost = sum(cost_matrix[r][c] for r, c in zip(row_ind, col_ind))
        print(f"Total cost: {total_cost}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
