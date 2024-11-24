def is_safe(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, N):
    # If all queens are placed, return True
    if row >= N:
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_nqueens_util(board, row + 1, N):
                return True

            # Backtrack if placing queen here doesn't lead to a solution
            board[row][col] = 0

    return False


def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return False

    print("Solution:")
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
    return True


# Example usage:
n = 8  # Number of queens
solve_nqueens(n)
