# script to play tic-tac-toe against the computer in the console
import random
from colorama import Fore, Back, Style

# add it lights up the color of the winning moves when someone moves
print(Fore.RED + 'some red text')

print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

coords = [' ',' ' ,' ',' ',' ',' ',' ',' ',' ']
winning_moves = []

computer_win = False
player_win = False

def drawboard():
    print(coords[0], '|',coords[1], '|',coords[2])
    print('-' * 10)
    print(coords[3], '|',coords[4], '|',coords[5])
    print('-' * 10)
    print(coords[6], '|',coords[7], '|',coords[8])

    if computer_win == True or player_win == True:
        index1 = winning_moves[0]
        index2 = winning_moves[1]
        index3 = winning_moves[2]
        print(coords[index1])
        print(coords[index2])
        print(coords[index3])



def one_round():
    player_move = int(input('Where would you like to play, coordinates are 1-9: '))
    #while True:
        #if coords[player_move-1] != ' ':
            #print("you cannot move there, try again: ")
            #player_move = int(input('Where would you like to play, coordinates are 1-9: '))
        #else:
            #break

    while True:
        computer_move = random.randint(1,9) 
        if coords[computer_move-1] == ' ':
            break

    coords[player_move-1] = 'x'
    coords[computer_move-1] = 'o'
    drawboard()

def wincheck():
    global player_win
    global computer_win
    global winning_moves
    for i in range(0,9,3):
        if coords[i] == coords[i+1] and coords[i+1] == coords[i+2]:
            if coords[i] == 'x':
                player_win = True
                print(Fore.RED, 'runjn')
                winning_moves = [i, i+1, i+2]
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


playgame()
