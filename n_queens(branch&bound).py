def solve_bb(n):
    board = [['.' for _ in range(n)] for _ in range(n)]

    cols = [False] * n
    diag1 = [False] * (2*n - 1)
    diag2 = [False] * (2*n - 1)

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if not cols[col] and not diag1[row-col+n-1] and not diag2[row+col]:

                # Place queen
                board[row][col] = 'Q'
                cols[col] = True
                diag1[row-col+n-1] = True
                diag2[row+col] = True

                if solve(row + 1):
                    return True

                # Backtrack
                board[row][col] = '.'
                cols[col] = False
                diag1[row-col+n-1] = False
                diag2[row+col] = False

        return False

    if solve(0):
        print("\nBranch & Bound Solution:")
        for row in board:
            print(" ".join(row))
    else:
        print("No solution")


# ---- Main ----
n = int(input("Enter N: "))
solve_bb(n)