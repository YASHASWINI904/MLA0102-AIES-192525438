graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(heuristic[start], start)]
visited = []

while open_list:
    open_list.sort()
    h, node = open_list.pop(0)

    if node not in visited:
        visited.append(node)

        if node == goal:
            print("Path:", visited)
            break

        for i in graph[node]:
            if i not in visited:
                open_list.append((heuristic[i], i))
