import sys

def tsp(cost, n):
    visited = [False] * n
    min_cost = [sys.maxsize]

    def solve(curr, count, cost_so_far):
        # If all cities visited and return to start
        if count == n and cost[curr][0] > 0:
            total_cost = cost_so_far + cost[curr][0]
            min_cost[0] = min(min_cost[0], total_cost)
            return

        for i in range(n):
            if not visited[i] and cost[curr][i] > 0:
                visited[i] = True

                # Branch and Bound (prune if already worse)
                if cost_so_far + cost[curr][i] < min_cost[0]:
                    solve(i, count + 1, cost_so_far + cost[curr][i])

                visited[i] = False   # backtrack

    visited[0] = True
    solve(0, 1, 0)

    return min_cost[0]


# Main
n = int(input("Enter number of cities: "))

cost = []
print("Enter cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

result = tsp(cost, n)
print("Minimum travelling cost:", result)