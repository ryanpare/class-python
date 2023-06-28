#!/usr/bin/env python3

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

col = int(input("X player, select a column: "))
row = int(input("X player, select a row: "))

board[row][col] = "X"
print(board[0])
print(board[1])
print(board[2])