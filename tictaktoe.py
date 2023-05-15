# script to play tic-tac-toe against the computer in the console

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
    drawboard()
    wincheck()
    if player_win:
        drawboard()
        print('You win!')
        return
    if ' ' not in coords:
        drawboard()
        print('tie')
    
    ai_move = minmax(coords, True)  # Pass True for the maximizing player (computer)
    print(f'Computer moves to {ai_move + 1}:')
    coords[ai_move] = '0'
    drawboard()
    wincheck()
    if computer_win:
        print('You lose')
        return

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
        if player_win or computer_win or ' ' not in coords:
            break



def getempty(coords):
    empty = [index for index, item in enumerate(coords) if item == ' ']
    return empty 



def minmax(coords, maximizing_player):
    available_coords = getempty(coords)

    if player_win:
        return -1
    elif computer_win:
        return 1
    elif len(available_coords) == 0:
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_coords:
            coords[move] = 'o'
            eval = minmax(coords, False)
            coords[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_coords:
            coords[move] = 'x'
            eval = minmax(coords, True)
            coords[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


playgame()

