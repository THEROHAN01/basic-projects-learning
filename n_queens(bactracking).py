def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_bt(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'

            if solve_bt(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = '.'

    return False


# ---- Main ----
n = int(input("Enter N: "))
board = [['.' for _ in range(n)] for _ in range(n)]

if solve_bt(board, 0, n):
    print("\nBacktracking Solution:")
    for row in board:
        print(" ".join(row))
else:
    print("No solution")