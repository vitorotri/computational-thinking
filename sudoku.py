# BSD 0-Clause License

# Copyright (c) 2025 Vito Romanelli Tricanico

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.



# Program that solves a Sudoku puzzle, using backtracking. User may input its own puzzle in the board list.

def is_valid(board, row, col, num):
    # Check if num already exists in the same row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if num already exists in the same column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if num already exists in the same subgrid
    subgrid_row = 3 * (row // 3)
    subgrid_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[subgrid_row + i][subgrid_col + j] == num:
                return False

    return True
    
     
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None
    
    
def solve_sudoku(board):
    empty = find_empty_cell(board)
    
    # Base case: no empty cells remain
    if not empty:
        return True
    
    row, col = empty
    
    # place number from 1 to 9 into board using empty (row, col) position
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack: reset the cell if no solution found
            
    return False


def print_sudoku(board):
	for i in range(9):
		if (i == 3 or i == 6):
			print('\n' * 2)
		else:
			print('\n' * 1)
		for j in range(9):
			if (j == 2 or j == 5):
				print(str(board[i][j]) + "   ", end="")
			else:
				print(str(board[i][j]) + " ", end="")
	print('\n' * 2)



# main

board = [
    [5, 3, 0,   0, 7, 0,   0, 0, 0],
    [6, 0, 0,   1, 9, 5,   0, 0, 0],
    [0, 9, 8,   0, 0, 0,   0, 6, 0],
    
    [8, 0, 0,   0, 6, 0,   0, 0, 3],
    [4, 0, 0,   8, 0, 3,   0, 0, 1],
    [7, 0, 0,   0, 2, 0,   0, 0, 6],
    
    [0, 6, 0,   0, 0, 0,   2, 8, 0],
    [0, 0, 0,   4, 1, 9,   0, 0, 5],
    [0, 0, 0,   0, 8, 0,   0, 7, 9]
]

print('\nInitial puzzle:\n')
print_sudoku(board)
solve_sudoku(board)
print('\nSolved puzzle:\n')
print_sudoku(board)
