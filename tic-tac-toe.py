def display_board(board):
    print('\n' * 100)

    print(board[7]+'|'+board[8]+'|'+ board[9])
    print(board[4]+'|'+board[5]+'|'+ board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])\

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


def player_input():

    """
    OUTPUT = (Player 1 marker, Player 2 marker)
    """

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')                #return some sort of tuple assignment ? what's this
    else:
        return ('O','X')

player_input()
