# Работа №9
## Решение задачи распределния ресурсов

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
|0|0|0|0|0|0|0|
|1|3|4|7|7|2|3|
|2|4|3|5|8|1|2|
|3|8|5|1|9|2|5|
|4|2|7|2|4|9|6|
|5|9|3|3|6|2|9|
|6|4|7|5|9|1|1|

$\phi_1(x)=\max\{f_1(x_1) \colon x_1 \in \overline{0,x}\}$
$\phi_1(0)=0, x_1^0=0$
$\phi_1(1)=3, x_1^0=1$
$\phi_1(2)=4, x_1^0=2$
$\phi_1(3)=8, x_1^0=3$
$\phi_1(4)=8, x_1^0=3$
$\phi_1(5)=9, x_1^0=5$
$\phi_1(6)=9, x_1^0=5$

$\phi_2(x)=\max\{f_2(x_2) + \phi_1(x - x_2)\colon x_2\in \overline{0,x}\}$
Current set: (3, 4)
$\phi_2(1)=4, x_2^0=1$
Current set: (4, 7, 3)
$\phi_2(2)=7, x_2^0=1$
Current set: (8, 8, 6, 5)
$\phi_2(3)=8, x_2^0=0$
Current set: (8, 12, 7, 8, 7)
$\phi_2(4)=12, x_2^0=1$
Current set: (9, 12, 11, 9, 10, 3)
$\phi_2(5)=12, x_2^0=1$
Current set: (9, 13, 11, 13, 11, 6, 7)
$\phi_2(6)=13, x_2^0=1$

$\phi_3(x)=\max\{f_3(x_3) + \phi_2(x - x_3)\colon x_3\in \overline{0,x}\}$
Current set: (4, 7)
$\phi_3(1)=7, x_3^0=1$
Current set: (7, 11, 5)
$\phi_3(2)=11, x_3^0=1$
Current set: (8, 14, 9, 1)
$\phi_3(3)=14, x_3^0=1$
Current set: (12, 15, 12, 5, 2)
$\phi_3(4)=15, x_3^0=1$
Current set: (12, 19, 13, 8, 6, 3)
$\phi_3(5)=19, x_3^0=1$
Current set: (13, 19, 17, 9, 9, 7, 5)
$\phi_3(6)=19, x_3^0=1$

$\phi_4(x)=\max\{f_4(x_4) + \phi_3(x - x_4)\colon x_4\in \overline{0,x}\}$
Current set: (7, 7)
$\phi_4(1)=7, x_4^0=0$
Current set: (11, 14, 8)
$\phi_4(2)=14, x_4^0=1$
Current set: (14, 18, 15, 9)
$\phi_4(3)=18, x_4^0=1$
Current set: (15, 21, 19, 16, 4)
$\phi_4(4)=21, x_4^0=1$
Current set: (19, 22, 22, 20, 11, 6)
$\phi_4(5)=22, x_4^0=1$
Current set: (19, 26, 23, 23, 15, 13, 9)
$\phi_4(6)=26, x_4^0=1$

$\phi_5(x)=\max\{f_5(x_5) + \phi_4(x - x_5)\colon x_5\in \overline{0,x}\}$
Current set: (7, 2)
$\phi_5(1)=7, x_5^0=0$
Current set: (14, 9, 1)
$\phi_5(2)=14, x_5^0=0$
Current set: (18, 16, 8, 2)
$\phi_5(3)=18, x_5^0=0$
Current set: (21, 20, 15, 9, 9)
$\phi_5(4)=21, x_5^0=0$
Current set: (22, 23, 19, 16, 16, 2)
$\phi_5(5)=23, x_5^0=1$
Current set: (26, 24, 22, 20, 23, 9, 1)
$\phi_5(6)=26, x_5^0=0$

$\phi_6(x)=\max\{f_6(x_6) + \phi_5(x - x_6)\colon x_6\in \overline{0,x}\}$
Current set: (7, 3)
$\phi_6(1)=7, x_6^0=0$
Current set: (14, 10, 2)
$\phi_6(2)=14, x_6^0=0$
Current set: (18, 17, 9, 5)
$\phi_6(3)=18, x_6^0=0$
Current set: (21, 21, 16, 12, 6)
$\phi_6(4)=21, x_6^0=0$
Current set: (23, 24, 20, 19, 13, 9)
$\phi_6(5)=24, x_6^0=1$
Current set: (26, 26, 23, 23, 20, 16, 1)
$\phi_6(6)=26, x_6^0=0$

6->0 $S=6$ 5->0 $S=6$ 4->1 $S=5$ 3->1 $S=4$ 2->1 $S=3$ 1->3 $S=0$ $x^o=(3, 1, 1, 1, 0, 0)$
$8+4+7+7+0+0 = 26$
### Программа для решения
```python
import random  
  
def generate_random_matrix(n):  
    matrix = [[random.randint(1, 9) for j in range(n)] for i in range(n)]  
    return matrix  
  
def print_markdown_matrix(matrix):  
    m = len(matrix[0])  
    print("| " * m + "|")  
    print("| --- " * m + "|")  
    for i in range(len(matrix)):  
        print(f"|", end='')  
        for j in range(len(matrix[i])):  
            print(matrix[i][j], end='|')  
        print()  
    print()  
  
def input_matrix(n):  
    matrix = []  
    for i in range(n):  
        row = list(map(int, input().split()))  
        matrix.append(row)  
    return matrix  
  
def main():  
    generate = input()  
    N = int(input())  
    n = N + 1  
    if generate:  
        matrix = generate_random_matrix(n)  
    else:  
        matrix = input_matrix(n)  
    for i in range(n):  
        matrix[i][0] = i  
    for j in range(n):  
        matrix[0][j] = 0  
    print_markdown_matrix(matrix)  
    phi = [[0 for j in range(n)] for i in range(n)]  
    x_ = [[0] * n for _ in range(n)]  
    print(r"$\phi_1(x)=\max\{f_1(x_1) \colon x_1 \in \overline{0,x}\}$")  
    for x in range(n):  
        set_ = [matrix[i][1] for i in range(x + 1)]  
        for item_number in range(len(set_)):  
            if set_[item_number] > set_[x_[1][x]]:  
                x_[1][x] = item_number  
        phi[1][x] = max(phi[1][x - 1], matrix[x][1])  
        print(fr"$\phi_1({x})={phi[1][x]}, x_1^0={x_[1][x]}$")  
    print()  
    for number in range(2, n):  
        print(rf"$\phi_{number}(x)=\max" + r"\{" + fr"f_{number}(x_{number}) + \phi_{number - 1}(x - x_{number})" + r"\colon " +  f"x_{number}"  + r"\in \overline{0,x}\}$")  
        for x in range(1, n):  
            set_ = [matrix[i][number] + phi[number - 1][x - i] for i in range(x + 1)]  
            for item_number in range(len(set_)):  
                if set_[item_number] > set_[x_[number][x]]:  
                    x_[number][x] = item_number  
            phi[number][x] = max(set_)  
            print(f"Current set: {tuple(set_)}")  
            print(fr"$\phi_{number}({x})={phi[number][x]}, x_{number}^0={x_[number][x]}$")  
        print()  
    S = N  
    i = N  
    x_o = [0] * n  
    while S > 0:  
        x_o[i] = x_[i][S]  
        print(f"{i}->{x_[i][S]}")  
        S -= x_[i][S]  
        print(f"$S={S}$")  
        i -= 1  
    print(f"$x^o=({", ".join(map(str, x_o[1:]))})$")  
    print("$" + "+".join(str(matrix[x_o[i]][i]) for i in range(1, n)) + f" = {phi[N][N]}$")  
  
  
if __name__ == "__main__":  
    main()
```
