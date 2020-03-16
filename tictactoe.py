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
#printBoard(theBoard)

turn='X'
for i in range(9):
    printBoard(theBoard)
    print('Kolej na '+ turn + '. Wybierz pole:')
    move = input()
    if theBoard[move.lower()] == ' ':
        theBoard[move.lower()] = turn
    else:
        print('\nTo pole jest zajęte! Tracisz turę.\n')
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
#    printBoard(theBoard)
