	Колесников М.Л. Б22-534

# Работа №10
## Задача о рюкзаке
Имеется рюкзак грузоподъемностью W.
$weight_i$ – вес одного предмета i-ого типа
$cost_i$ – стоимость (ценность) одного предмета i-ого типа
$x_i$ – число предметов i-ого типа, которые будут загружаться на транспортировочное средство. Требуется заполнить его грузом, состоящим из предметов N различных типов таким образом, чтобы стоимость (ценность) всего груза была максимальной.
$$
\Large
\begin{aligned}
W(x)=\sum_{i=1}^{N} x_i \cdot cost_i \rightarrow max \\
\sum_{i=1}^{N} x_i \cdot weight_i \leq W, \quad x_i \in \{0\} \cup \mathbb{N}
\end{aligned}
$$
Решение задачи разбивается на N этапов. На каждом i-ом этапе определяется максимальная стоимость груза, состоящего из предметов типа $k=\overline{1,i}$
##### Рекуррентное уравнение Беллмана для задачи о рюкзаке
$W_i(weight)$ - максимальная стоимость груза, состоящего из предметов типа $k=\overline{1,i}$ с общим весом не более $weight$.
$$
\Large
\begin{aligned}
& \forall \ weight \colon \ weight \in \overline{0,W} \\
& W_i(weight) = \max_{x_i \in \overline{0, \left[\frac{weight}{weight_i}\right]}} \{x_i \cdot cost_i + W_{i-1}(weight - x_i \cdot weight_i)\} \\
& \forall \ weight \colon weight \in \overline{0,W} \quad  W_0(weight)=0
\end{aligned}
$$
### Решение
Дано: N=6, W=20

| weight | 5   | 9   | 8   | 7   | 10  | 13  |
| ------ | --- | --- | --- | --- | --- | --- |
| cost   | 28  | 20  | 13  | 6   | 21  | 18  |
Шаг №1:
$$
\large \begin{aligned}
& W_1(0)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_1 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(1)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_1 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(2)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_1 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(3)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_1 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(4)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_1 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(5)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28\}= 28, \quad x_1 = 1 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(6)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28\}= 28, \quad x_1 = 1 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(7)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28\}= 28, \quad x_1 = 1 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(8)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28\}= 28, \quad x_1 = 1 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(9)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28\}= 28, \quad x_1 = 1 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(10)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56\}= 56, \quad x_1 = 2 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(11)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56\}= 56, \quad x_1 = 2 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(12)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56\}= 56, \quad x_1 = 2 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(13)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56\}= 56, \quad x_1 = 2 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(14)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56\}= 56, \quad x_1 = 2 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(15)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84\}= 84, \quad x_1 = 3 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(16)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84\}= 84, \quad x_1 = 3 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(17)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84\}= 84, \quad x_1 = 3 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(18)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84\}= 84, \quad x_1 = 3 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(19)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84\}= 84, \quad x_1 = 3 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_1(20)=\max_{x_i \in \overline{0, \left[\frac{20}{5}\right]}} \{x_i \cdot cost_i + W_{1-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0, 28, 56, 84, 112\}= 112, \quad x_1 = 4 \\
\end{aligned}
$$
Шаг №2:
$$
\large \begin{aligned}
& W_2(0)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(1)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(2)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(3)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(4)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(5)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(6)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(7)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(8)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(9)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 20\}= 28, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(10)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 20\}= 56, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(11)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 20\}= 56, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(12)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 20\}= 56, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(13)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 20\}= 56, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(14)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 48\}= 56, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(15)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 48\}= 84, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(16)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 48\}= 84, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(17)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 48\}= 84, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(18)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 48, 40\}= 84, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(19)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 76, 40\}= 84, \quad x_2 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_2(20)=\max_{x_i \in \overline{0, \left[\frac{20}{9}\right]}} \{x_i \cdot cost_i + W_{2-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
112, 76, 40\}= 112, \quad x_2 = 0 \\
\end{aligned}
$$
Шаг №3:
$$
\large \begin{aligned}
& W_3(0)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(1)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(2)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(3)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(4)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(5)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(6)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(7)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(8)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 13\}= 28, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(9)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 13\}= 28, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(10)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 13\}= 56, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(11)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 13\}= 56, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(12)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 13\}= 56, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(13)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 41\}= 56, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(14)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 41\}= 56, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(15)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 41\}= 84, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(16)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 41, 26\}= 84, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(17)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 41, 26\}= 84, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(18)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 69, 26\}= 84, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(19)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 69, 26\}= 84, \quad x_3 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_3(20)=\max_{x_i \in \overline{0, \left[\frac{20}{8}\right]}} \{x_i \cdot cost_i + W_{3-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
112, 69, 26\}= 112, \quad x_3 = 0 \\
\end{aligned}
$$
Шаг №4:
$$
\large \begin{aligned}
& W_4(0)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(1)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(2)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(3)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(4)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(5)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(6)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(7)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 6\}= 28, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(8)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 6\}= 28, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(9)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28, 6\}= 28, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(10)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 6\}= 56, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(11)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 6\}= 56, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(12)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 34\}= 56, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(13)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 34\}= 56, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(14)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 34, 12\}= 56, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(15)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 34, 12\}= 84, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(16)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 34, 12\}= 84, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(17)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 62, 12\}= 84, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(18)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 62, 12\}= 84, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(19)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 62, 40\}= 84, \quad x_4 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_4(20)=\max_{x_i \in \overline{0, \left[\frac{20}{7}\right]}} \{x_i \cdot cost_i + W_{4-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
112, 62, 40\}= 112, \quad x_4 = 0 \\
\end{aligned}
$$
Шаг №5:
$$
\large \begin{aligned}
& W_5(0)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(1)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(2)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(3)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(4)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(5)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(6)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(7)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(8)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(9)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(10)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 21\}= 56, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(11)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 21\}= 56, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(12)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 21\}= 56, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(13)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 21\}= 56, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(14)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 21\}= 56, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(15)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 49\}= 84, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(16)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 49\}= 84, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(17)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 49\}= 84, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(18)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 49\}= 84, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(19)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 49\}= 84, \quad x_5 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_5(20)=\max_{x_i \in \overline{0, \left[\frac{20}{10}\right]}} \{x_i \cdot cost_i + W_{5-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
112, 77, 42\}= 112, \quad x_5 = 0 \\
\end{aligned}
$$
Шаг №6:
$$
\large \begin{aligned}
& W_6(0)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(1)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(2)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(3)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(4)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
0\}= 0, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(5)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(6)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(7)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(8)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(9)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
28\}= 28, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(10)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56\}= 56, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(11)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56\}= 56, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(12)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56\}= 56, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(13)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 18\}= 56, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(14)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
56, 18\}= 56, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(15)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 18\}= 84, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(16)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 18\}= 84, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(17)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 18\}= 84, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(18)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 46\}= 84, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(19)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
84, 46\}= 84, \quad x_6 = 0 \\
\end{aligned}
$$
$$
\large \begin{aligned}
& W_6(20)=\max_{x_i \in \overline{0, \left[\frac{20}{13}\right]}} \{x_i \cdot cost_i + W_{6-1}(20 - x_i \cdot weight_i)\}= \\& = \max \{
112, 46\}= 112, \quad x_6 = 0 \\
\end{aligned}
$$
###### Ответ
Максимальная стоимость: 112
$W_6(20)$ при $x_6^o=0$
$W_5(20 - 0 * 13)=112$ при $x_5^o=0$
$W_4(20 - 0 * 10)=112$ при $x_4^o=0$
$W_3(20 - 0 * 7)=112$ при $x_3^o=0$
$W_2(20 - 0 * 8)=112$ при $x_2^o=0$
$W_1(20 - 0 * 9)=112$ при $x_1^o=4$
Оптимальное решение: (4, 0, 0, 0, 0, 0)
##  Решение программой:
```python
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
    
n, w, weight, cost = get_problem_from_file("Work10/input2.txt")  
print(f"Количество типов предметов {n}, грузоподъемность: {w}")  
print("Веса:")  
print_markdown_matrix([weight[1:]])  
print("Стоимости:")  
print_markdown_matrix([cost[1:]])  
print("Решение:")  
knapsack(n, w, weight, cost)  
```
