from collections import deque

CAP1 = 11
CAP2 = 9
GOAL = 8

def bfs():
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if a == GOAL or b == GOAL:
            return path + [(a, b)]

        if (a, b) in visited:
            continue

        visited.add((a, b))

        next_states = []

        # Fill Jug 1
        next_states.append((CAP1, b))

        # Fill Jug 2
        next_states.append((a, CAP2))

        # Empty Jug 1
        next_states.append((0, b))

        # Empty Jug 2
        next_states.append((a, 0))

        # Pour Jug 1 -> Jug 2
        transfer = min(a, CAP2 - b)
        next_states.append((a - transfer, b + transfer))

        # Pour Jug 2 -> Jug 1
        transfer = min(b, CAP1 - a)
        next_states.append((a + transfer, b - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [(a, b)]))

    return None

solution = bfs()

print("Sequence of States:")
for state in solution:
    print(state)

print("\nGoal Achieved: Exactly 8 litres measured.")
