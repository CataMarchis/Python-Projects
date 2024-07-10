import random

def display_board(board):

    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print(' --------- ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print(' --------- ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')


def player_input():
    marker = ''

    while (marker != 'X' and marker != 'O'):
        marker = input('Player 1, your marker between X and O is: ')
    player1 = marker

    if(player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)


def place_marker(board, marker, position):
    if(position in range(1,10)):
        board[position] = marker
    return board


def win_check(board, mark):
    if(board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or
       board[7] == board[8] == board[9] == mark or board[7] == board[4] == board[1] == mark or
       board[8] == board[5] == board[2] == mark or board[9] == board[6] == board[3] == mark or
       board[1] == board[5] == board[9] == mark or board[7] == board[5] == board[3] == mark):
        print(f'The game is over, {mark} has won!')
        return True
    print('The game is still going!')
    return False


def choose_first():
    result = random.randint(1,2)
    if(result == 1):
        return('Player 1')
    else:
        return('Player 2')
    

def space_check(board, position):
    if(board[position] == ' '):
        return True
    else:
        return False
    

def full_board_check(board):
    for element in board:
        if(element == ' '):
            return False
        else:
            pass
    return True


def player_choice(board):
    position = ' '
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board, position) == False:
        position = int(input('Give me your next position(1-9): '))

    return position


def replay():
    ask = input('Do you wanna play again? y or n? ')
    if(ask == 'y'):
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    the_board = ['#' , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    play_game = input('Ready to play? y or n?')

    if(play_game == 'y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
