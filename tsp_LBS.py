# Cities
cities = ["A", "B", "C", "D"]

# Distance between cities
distance = {
    ("A", "B"): 10,
    ("A", "C"): 10,
    ("A", "D"): 20,
    ("B", "C"): 35,
    ("B", "D"): 20,
    ("C", "D"): 30
}

# Calculate distance between two cities
def get_distance(a, b):
    if (a, b) in distance:
        return distance[(a, b)]
    else:
        return distance[(b, a)]


# Calculate total route distance
def route_distance(route):
    total = 0

    for i in range(len(route)):
        total += get_distance(
            route[i], route[(i + 1) % len(route)]
        )

    return total


# Generate new routes
def get_neighbors(route):
    neighbors = []

    for i in range(1, len(route)):
        new_route = route.copy()

        new_route[1], new_route[i] = new_route[i], new_route[1]

        neighbors.append(new_route)

    return neighbors


# Local Beam Search
def local_beam_search():

    beam = [
        ["A", "B", "C", "D"],
        ["A", "C", "B", "D"]
    ]

    for i in range(5):

        print("\nIteration:", i + 1)

        new_routes = []

        for route in beam:
            new_routes.extend(get_neighbors(route))

        new_routes.sort(key=route_distance)

        beam = new_routes[:2]

        for route in beam:
            print(route, route_distance(route))

    best = min(beam, key=route_distance)

    print("\nBest Route:", best)
    print("Total Distance:", route_distance(best))


local_beam_search()