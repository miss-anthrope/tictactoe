#!/usr/bin/env python
# coding: utf-8


# This is the start of the game. Step 1, print the board.

def display_board(board):
    # print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
# Step 2, choose the markers.

def player_input():
    
    marker = ''
    
    #Keep asking for X or O
   
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()
    
    #Assign Player2 the opposite marker of Player1
    
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

# Step 3, take the board, the marker, and the position in

def place_marker(board, marker, position):
    board[position] = marker
    
# Step 4, check for a winner

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # this is for top row across
    (board[4] == mark and board[5] == mark and board[6] == mark) or # this is for middle row across
    (board[1] == mark and board[2] == mark and board[3] == mark) or # this is bottom row across
    (board[7] == mark and board[4] == mark and board[1] == mark) or # this is left down
    (board[8] == mark and board[5] == mark and board[2] == mark) or # this is middle down
    (board[9] == mark and board[6] == mark and board[3] == mark) or # this is right down
    (board[7] == mark and board[5] == mark and board[3] == mark) or # this is diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # this is also diagonal

# Step 5, randomly select which player goes first

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
# Step 6, write a function that returns a boolean answer if a position is free

def space_check(board, position):
    return board[position] == ' '

# Step 7, check if the board is full with a boolean value; True = full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Step 8, have the player pick a position and use the space_check to see if it's free

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please enter your next position (1-9) '))
        
    return position

# Step 9, ask the player if they want to play another game

def replay():
    return input("Do you want to play again? Enter Y or N: ").lower().startswith('y')

# Step 10, using while loops to run the game

print("Welcome to Meag's tic-tac-toe!")

while True:
    #reset the board
    theBoard = [' '] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? (Y/N)')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == 'Player 1':
            # this defines Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congrats! You win!')
                game_on = False  
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Looks like a draw.')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            # this defines Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congrats! Player 2 won!')
                game_on = False
                
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Looks like a draw.')
                    break
                else:
                    turn = 'Player 1'
    
    if not replay():
        break




