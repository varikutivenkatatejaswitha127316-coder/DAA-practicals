def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
        return True

    return False


def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices

    edges.sort(key=lambda x: x[2])

    mst_cost = 0
    print("Edges in Minimum Spanning Tree:")

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            print(u, "-", v, ":", weight)
            mst_cost += weight

    print("Total MST Cost:", mst_cost)

vertices = 5

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

kruskal(vertices, edges)
