# script to play tic-tac-toe against the computer in the console
import random

coords = [' ',' ' ,' ',' ',' ',' ',' ',' ',' ',]

def drawboard():
    print(coords[0], '|',coords[1], '|',coords[2])
    print('-' * 10)
    print(coords[3], '|',coords[4], '|',coords[5])
    print('-' * 10)
    print(coords[6], '|',coords[7], '|',coords[8])

def one_round():
    player_move = int(input('Where would you like to play, coordinates are 1-9: '))
    coords[player_move-1] = 'x'
    computer_move = random.randint(1,9)

    while True:
        if coords[computer_move-1] != ' ':
            computer_move = random.randint(1,9)
        if coords[computer_move-1] == ' ':
            break
    
    coords[computer_move-1] = 'o'
    drawboard()

def wincheck():
    for i in range(7):
        if coords[i] == coords[i+1] and coords[i+1] == coords[i+2]:
            if coords[i] == 'x':
                return True
            elif coords[i] == 'o':
                return False
    
    for i in range(0,3):
        if coords[i] == coords[i+3] and coords[i+3] == coords[i+6]:
            if coords[i] == 'x':
                return True
            elif coords[i] == 'o':
                return False
    
    if coords[1] == coords[5] and coords[5] == coords[9]:
        if coords[1] == 'x':
            return True
        elif coords[1] == 'o':
                return False

    if coords[3] == coords[5] and coords[5] == coords[7]:
        if coords[3] == 'x':
            return True
        elif coords[3] == 'o':
                return False
    



one_round()
one_round()
one_round()
wincheck()
one_round()
wincheck()
one_round()

