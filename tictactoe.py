from tictactoe_winner import checkwinner

theBoard = {'top-l':' ','top-m':' ','top-r':' ',
            'mid-l':' ','mid-m':' ','mid-r':' ',
            'low-l':' ','low-m':' ','low-r':' '}

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
    print('\n')

turn='X'
gameon=True
while gameon==True:

    printBoard(theBoard)
    print('Kolej na '+ turn + '. Wybierz pole:')
    move = input().lower()

    if move in theBoard:

        if theBoard[move] == ' ':
            theBoard[move] = turn
        else:
            print('\nTo pole jest zajęte! Tracisz turę.\n')
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    else:
        print('\nTakie pole nie istnieje. Spróbuj jeszcze raz.\n')

    gameon = checkwinner(theBoard)

printBoard(theBoard)
