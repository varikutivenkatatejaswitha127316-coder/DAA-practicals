from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

start = 0

min_cost = float('inf')

best_path = []

for path in permutations(range(n)):
    
    if path[0] == start:
        
        cost = 0

        for i in range(n - 1):
            cost += graph[path[i]][path[i + 1]]

        cost += graph[path[-1]][start]

        if cost < min_cost:
            min_cost = cost
            best_path = list(path) + [start]

print("Best Path:", best_path)
print("Minimum Travel Cost:", min_cost)
