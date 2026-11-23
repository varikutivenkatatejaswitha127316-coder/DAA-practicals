INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]
V = len(graph)

dist = [row[:] for row in graph]

for k in range(V):
    for i in range(V):
        for j in range(V):

            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

print("Shortest Distance Matrix:")

for i in range(V):
    for j in range(V):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
