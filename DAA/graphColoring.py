def is_safe(node, graph, color, c, n):
    for i in range(n):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True


def solve(node, graph, m, color, n):
    if node == n:
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c, n):
            color[node] = c

            if solve(node + 1, graph, m, color, n):
                return True

            color[node] = 0  # backtrack

    return False


def graph_coloring():
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix:")

    graph = []
    for i in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    m = int(input("Enter number of colors: "))

    color = [0] * n

    if solve(0, graph, m, color, n):
        print("Color assignment:", color)
    else:
        print("No solution")


graph_coloring()