def prim(graph, start):
    n = len(graph)

    selected = [False] * n
    selected[start] = True

    mst_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for _ in range(n - 1):
        min_weight = float('inf')
        u = -1
        v = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            u = i
                            v = j

        if u == -1:
            print("Graph is not connected")
            return

        print(u, "-", v, ":", min_weight)

        selected[v] = True
        mst_cost += min_weight

    print("Total MST Cost:", mst_cost)

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, 0)
