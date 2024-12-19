def knapsack(n: int, w: int, weight: list[int], cost: list[int]):
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    x_o = [[0] * (w + 1) for _ in range(n + 1)]
    for type_number in range(1, n + 1):
        print(f"Шаг №{type_number}:")
        for C in range(w + 1):
            print("$$")
            print(r"\large \begin{aligned}")
            print(fr"& W_{type_number}({C})=\max_" + r"{x_i \in \overline{0, \left[\frac{" + str(w) + "}{" + str(weight[type_number]) + r"}\right]}}" + r" \{", end='')
            print(r"x_i \cdot cost_i + W_{" + f"{type_number}-1" + "}(" + str(w) + r" - x_i \cdot weight_i)" + r"\}= \\", end='')
            dp[type_number][C] = dp[type_number - 1][C]  # when subject of type_number type is not taken
            print(r"& = \max \{")
            print(dp[type_number][C], end='')
            max_items = C // weight[type_number]  # max count of subject of type_number type
            for x in range(1, max_items + 1):
                cur = x * cost[type_number] + dp[type_number - 1][C - x * weight[type_number]]
                print(", " + str(cur), end='')
                if dp[type_number][C] < cur:
                    x_o[type_number][C] = x
                    dp[type_number][C] = cur
            print(r"\}=", rf"{dp[type_number][C]}, \quad x_{type_number} = {x_o[type_number][C]} \\")
            print(r"\end{aligned}")
            print("$$")
        # print_markdown_matrix([[i for i in range(w + 1)]] + [dp[type_number]] + [x_o[type_number]])
    print(f"###### Ответ")
    print(f"Максимальная стоимость: {dp[n][w]}")
    w_ = w
    x_optimal = [str(x_o[n][w_])]
    print(f"$W_{n}({w_})$ при $x_{n}^o={x_o[n][w_]}$")
    for n_ in range(n - 1, 0, -1):
        print(f"$W_{n_}({w_} - {x_o[n_ + 1][w_]} * {weight[n_ + 1]})=", end='')
        w_ -= x_o[n_ + 1][w_] * weight[n_ + 1]
        print(f"{dp[n_][w_]}$ при $x_{n_}^o={x_o[n_][w_]}$")
        x_optimal.append(str(x_o[n_][w_]))
    print("Оптимальное решение: (" + ", ".join(x_optimal[::-1]) + ")")

def print_markdown_matrix(matrix):
    m = len(matrix[0])
    print()
    print("| " * m + "|")
    print("| --- " * m + "|")
    for i in range(len(matrix)):
        print(f"|", end='')
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='|')
        print()
    print()

def get_problem_from_file(file_name):
    with open(file_name) as f:
        n, w = int(f.readline()), int(f.readline())
        weight = [-1] + list(map(int, f.readline().split()))
        cost = [-1] + list(map(int, f.readline().split()))
    return n, w, weight, cost

def main():
    n, w, weight, cost = get_problem_from_file("Work10/input2.txt")
    print(f"Количество типов предметов {n}, грузоподъемность: {w}")
    print("Веса:")
    print_markdown_matrix([weight[1:]])
    print("Стоимости:")
    print_markdown_matrix([cost[1:]])
    print("Решение:")
    knapsack(n, w, weight, cost)

if __name__ == "__main__":
    main()