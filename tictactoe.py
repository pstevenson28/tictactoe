#tic tac toe

"""
tic tac toe board
user_input -> something 1-9
if they enter anything else: tell them to go again
check if the user_input is already taken
add it to the board
check if the user has won, checking rows, columns and diagonals
switch between user and computer
"""

import random
import sys
board=[i for i in range(0,9)]
player, computer = '',''
# // Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# // Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# // Table
tab=range(1,10)

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def print_board(board):
    print(board[0] + " | " + (board)[1] + " | " + (board)[2])
    print(board[3] + " | " + (board)[4] + " | " + (board)[5])
    print(board[6] + " | " + (board)[7] + " | " + (board)[8])

print_board(board)

