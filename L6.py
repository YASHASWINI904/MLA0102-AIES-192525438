graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

open_list = [(heuristic[start], 0, start, [start])]
visited = []

while open_list:
    open_list.sort()
    f, g, node, path = open_list.pop(0)

    if node == goal:
        print("Optimal Path:", path)
        print("Total Cost:", g)
        break

    if node not in visited:
        visited.append(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append((new_f, new_g, neighbor, path + [neighbor]))