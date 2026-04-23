import heapq

goal_state = ((1,2,3),
              (4,5,6),
              (7,8,0))


def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def print_state(state):
    for row in state:
        print(row)
    print()


def get_neighbors(state):
    neighbors = []
    state = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def astar(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()
    step = 0

    while pq:
        f, g, current, path = heapq.heappop(pq)

        print(f"Step {step}")
        print("Current State:")
        print_state(current)
        print(f"g(n) = {g}, h(n) = {heuristic(current)}, f(n) = {f}")
        print("-" * 30)

        step += 1

        if current == goal_state:
            print("Goal Reached!\n")
            print("Final Path:")
            for state in path + [current]:
                print_state(state)
            return

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current])
                )


# ---- Start State ----
start_state = ((1,2,3),
               (4,0,6),
               (7,5,8))

astar(start_state)