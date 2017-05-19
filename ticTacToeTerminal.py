from tttlogic import *


def main():
    squares = ['NorthWest', 'North', 'NorthEast',
               'West',      'Center','East',
               'SouthWest', 'South',  'SouthEast']

    initialize_board()

    while check_status() == (None, 'Playing'):
        currentPlayer = current_player()
        print('Current Move:',currentPlayer,'\nSelect an available square\n')

        for i in squares:
            print(i,look(i))

        choice = input('\nChoose an empty sqaure: ')
        print(currentPlayer, 'played in', choice,'\n')
        
        if look(choice) != None:
            print('*****************\nError!\n*****************\n')
        
        else:
            move(choice)

    print(check_status())

    
initialize_board()

main()

again = input('Play again?: y or n\n')

if again == 'y':
    main()
else:
    exit()