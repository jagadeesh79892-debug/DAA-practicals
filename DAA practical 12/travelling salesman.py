
from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        cost = 0
        current = start

        for city in path:
            cost += graph[current][city]
            current = city

        cost += graph[current][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(path) + [start]

    print("Minimum Cost:", min_cost)
    print("Best Path:", best_path)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
