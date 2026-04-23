def is_safe(board, row, col, n):
    for i in range(n):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    return True


def solve(board, row, n, fixed_row):
    if row == n:
        return True

    if row == fixed_row:  # skip already placed queen
        return solve(board, row + 1, n, fixed_row)

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n, fixed_row):
                return True

            board[row][col] = 0

    return False


# Main
n = 8
board = [[0]*n for _ in range(n)]

r = int(input("Enter row of first queen (0-7): "))
c = int(input("Enter column of first queen (0-7): "))

board[r][c] = 1

if solve(board, 0, n, r):
    print("\nFinal Matrix:")
    for row in board:
        print(row)
else:
    print("No solution")