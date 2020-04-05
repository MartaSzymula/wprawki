def checkwinner(theBoard):
    Boardlist=[['top-l', 'top-m', 'top-r'], ['mid-l', 'mid-m', 'mid-r'], ['low-l', 'low-m', 'low-r'], ['low-l', 'mid-m', 'top-r'],
    ['top-l', 'mid-m', 'low-r'], ['top-l', 'mid-l', 'low-l'], ['top-m', 'mid-m', 'low-m'], ['top-r', 'mid-r', 'low-r'],]

    for i in ['X', 'O']:
        for condition in Boardlist:
            if theBoard[condition[0]]==i and theBoard[condition[1]]==i and theBoard[condition[2]]==i:
                print('\nKoniec gry. Wygrał gracz ' + i + '!\n')
                return False

    if ' ' in list(theBoard.values()):
        return True
    else:
        print('\nGra skończona. Nikt nie wygrał.\n')
        return False
