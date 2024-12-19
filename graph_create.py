import math
import networkx as nx
import matplotlib.pyplot as plt

from functions import input_matrix

adj = [[0, 1, 2, 3, 4, 6],
       [3, 0, 2, 1, 5, 6],
       [1, 2, 0, 3, 6, 6],
       [3, 2, 1, 0, 7, 6],
       [8, 9, 9, 8, 0, 6],
       [8, 9, 9, 8, 1, 0]]
N = 6

maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif(adj[i][j] <= second and adj[i][j] != first):
            second = adj[i][j]
    return second

decision_graph = nx.DiGraph()

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (adj[curr_path[level - 1]][i] != 0 and not visited[i]):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                decision_graph.add_node(tuple(curr_path[:level + 1]), cost=curr_weight)
                if level > 1:
                    decision_graph.add_edge(tuple(curr_path[:level]), tuple(curr_path[:level + 1]),
                                            weight=adj[curr_path[level - 1]][i])

                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i) + secondMin(adj, i))

    curr_bound = math.ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0

    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize

TSP(adj)

print("Minimum cost:", final_res)
print("Path Taken: ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')

pos = nx.nx_agraph.graphviz_layout(decision_graph, prog='dot')

edges = decision_graph.edges(data=True)
node_labels = {node: node[-1] for node in decision_graph.nodes()}

plt.figure(figsize=(20, 20))
nx.draw(decision_graph, pos, with_labels=True, node_color='red', node_size=1000, font_size=10)
nx.draw_networkx_edge_labels(decision_graph, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in edges}, font_color='red')

plt.title("Decision Tree for TSP")
plt.show()
