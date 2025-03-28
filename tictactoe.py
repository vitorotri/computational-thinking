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



# Program to play Tic-Tac-Toe in the terminal, where the A.I. uses the Minimax algorithm.

import numpy as np

def print_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")

# check if win happens
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        # if all given positions are equal and not empty, it is a win
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None
   
def minimax(board, depth, is_maximizing):
    # first evaluate if it is a terminal state
    if check_win(board) == 'X':
        return 10 - depth
    elif check_win(board) == 'O':
        return -10 + depth
    elif ' ' not in board:
        return 0
        
    # should also implement threats?

    if is_maximizing:
        best_score = -np.Inf
        for i in range(9):
            if board[i] == ' ':
                # test for empty board position (machine's turn)
                #
                # recursivelly builds tree
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
                # end test for empty board position
        return best_score
    else:
        best_score = np.Inf
        for i in range(9):
            if board[i] == ' ':
                # test for empty board position (machine test for human's turn)
                #
                # recursivelly builds tree
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
                # end test for empty board position
        return best_score

# uses minimax to find best move for A.I.
def find_best_move(board):
    best_score = np.Inf
    move = -1 # just for comparison in play_game()
    for i in range(9):
        # only if board position is empty
        if board[i] == ' ':
        
            # test for empty board position
            #
            # minimax for the player (minimizer): for each board position i, will find the one with highest
            # possible value amongst plays from the minimizer, assuming human plays optimally, choosing best
            # position
            #
            # recursivelly builds tree
            board[i] = 'O'
            score = minimax(board, 0, True)
            board[i] = ' '
            # end test for empty board position
            
            if score < best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    start = int(input("\nWho will start the game?\n\n1 - Player\n2 - Machine\n\n"))
    if start == 1:
    	player = 'X'
    elif start == 2:
    	player = 'O'
    else:
    	print("\nOption unkown, machine will start...\n")
    	player = 'O'

    while ' ' in board and check_win(board) is None:
        print_board(board)
        if player == 'X':
            move = int(input("\nEnter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                player = 'O'
        else:
            print("\nMachine's turn...")
            move = find_best_move(board)
            if move != -1:
                board[move] = 'O'
                player = 'X'
    
    print_board(board)
    if check_win(board) == 'X':
        print("\nYou win!\n")
    elif check_win(board) == 'O':
        print("\nMachine wins!\n")
    else:
        print("\nIt's a tie!\n")

play_game()
