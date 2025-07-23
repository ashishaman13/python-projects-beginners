from lib2to3.pytree import generate_matches


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

# display_game(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:        # why list items are in strings
        choice = input('Pick a position(0,1,2): ')

        if choice not in ['0','1','2']:
            print("Sorry, invalid choice")

    return int(choice)

#position_choice()


def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement            # Grab the game list at the position - meaning of this line

    return game_list




def gameon_choice():
    choice = 'wrong'

    while choice not in ['Y','N']:        # why list items are in strings
        choice = input('Keep Playing? (Y or N): ')

        if choice not in ['Y','N']:
            print("Sorry, I dont understand, please choose Y or N ")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()

