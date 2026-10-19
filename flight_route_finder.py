import heapq
from itertools import count

routes_explored = 0
def ucs_cheapest_route(graph, start, goal):
    global routes_explored
    routes_explored = 0

    priority = count()
    queue = [(0, next(priority), [start])]

    while queue:
        cost, _, path = heapq.heappop(queue)
        routes_explored += 1

        print("Exploring:", path, "| Cost:", cost)

        city = path[-1]

        if city == goal:
            return path, cost

        for next_city, ticket_price in graph.get(city, []):
            if next_city not in path:
                new_path = path + [next_city]
                new_cost = cost + ticket_price

                heapq.heappush(
                    queue,
                    (new_cost, next(priority), new_path)
                )

    return [], float("inf")

flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

route, total_cost = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

print("Cheapest route:", route)
print("Total ticket cost:", total_cost)
