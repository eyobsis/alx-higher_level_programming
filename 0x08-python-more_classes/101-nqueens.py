#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    """Solve the N-queens problem using backtracking."""
    # Base case: If all queens are placed, print the solution
    if col == n:
        print_solution(board, n)
        return

    # Consider this column and try placing a queen in all rows
    for row in range(n):
        if is_safe(board, row, col, n):
            # Place the queen in board[row][col]
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1, n)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0


def print_solution(board, n):
    """Print the N-queens solution."""
    solution = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)
