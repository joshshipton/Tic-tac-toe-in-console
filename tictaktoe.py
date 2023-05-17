# script to play tic-tac-toe against the computer in the console
import random

coords = [' ',' ' ,' ',' ',' ',' ',' ',' ',' ']

computer_win = False
player_win = False

def drawboard():
    print(coords[0], '|',coords[1], '|',coords[2])
    print('-' * 10)
    print(coords[3], '|',coords[4], '|',coords[5])
    print('-' * 10)
    print(coords[6], '|',coords[7], '|',coords[8])

def one_round():
    player_move = int(input('Where would you like to play, coordinates are 1-9: '))
    while True:
        if coords[player_move-1] != ' ':
            print("you cannot move there, try again: ")
            player_move = int(input('Where would you like to play, coordinates are 1-9: '))
        else:
            break

    coords[player_move-1] = 'x'

    while True:
        if ' ' not in coords:
            break
        computer_move = computermove(coords, True)
        best_computer_move = computer_move[1]
        if coords[best_computer_move] == ' ' and computer_move != player_move:
            coords[best_computer_move] = 'o'
            break


    drawboard()

def wincheck():
    global player_win
    global computer_win
    for i in range(0,9,3):
        if coords[i] == coords[i+1] and coords[i+1] == coords[i+2]:
            if coords[i] == 'x':
                player_win = True
            elif coords[i] == 'o':
                computer_win = True

    for i in range(0,3):
        if coords[i] == coords[i+3] and coords[i+3] == coords[i+6]:
            if coords[i] == 'x':
                player_win = True
            elif coords[i] == 'o':
                computer_win = True

    if coords[0] == coords[4] and coords[4] == coords[8]:
        if coords[4] == 'x':
            player_win = True

        elif coords[4] == 'o':
            computer_win = True


    if coords[2] == coords[4] and coords[4] == coords[6]:
        if coords[4] == 'x':
            player_win = True

        elif coords[4] == 'o':
            computer_win = True


def playgame():
    while True:
        one_round()
        wincheck()
        if player_win == True:
            drawboard()
            return print("You win!")
        elif computer_win:
            drawboard()
            return print("You lose! :(")
        if ' ' not in coords:
            return print('Tie :/')
        
def getempty(coords):
    empty = [index for index, item in enumerate(coords) if item == ' ']
    return empty 

# using the minmax algorithm 
def computermove(coords, player):
    global player_win
    global computer_win
    
    available = getempty(coords)
    wincheck()
    
    if player_win:
        player_win = False
        return -1, None
    if computer_win:
        computer_win = False
        return 1, None
    if len(available) == 0:
        return 0, None
    
    if player:
        max_eval = float('-inf')
        best_move = None
        
        for move in available:
            coords[move] = 'o'
            eval_score, _ = computermove(coords, False)
            coords[move] = ' '
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move
        
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        
        for move in available:
            coords[move] = 'x'
            eval_score, _ = computermove(coords, True)
            coords[move] = ' '
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move
        
        return min_eval, best_move


playgame()
