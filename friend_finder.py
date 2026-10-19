from collections import deque
network = {
    "Ali": ["Bilal", "Sara", "Ahmed"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
    "Ahmed": ["Ali"]
}

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = [start]
    while queue:
        path = queue.popleft()
        person = path[-1]

        if person == goal:
            return path

        for friend in graph[person]:
            if friend not in visited:
                visited.append(friend)
                queue.append(path + [friend])

    return None

path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print("Shortest chain from Ali to Hira:", path)
    print("Number of introductions needed:", len(path) - 1)
else:
    print("No connection found")
