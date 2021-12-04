HEIGHT = 5
WIDTH = 5

"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""

def bingo(board, newNum):
    for row in range(HEIGHT):
        bingo = 0
        for col in range(WIDTH):
            if(board[row][col] == -1 or board[row][col] == newNum):
                bingo+=1
                board[row][col] = -1
        if(bingo == HEIGHT):
            return True    

    for row in range(HEIGHT):
            bingo = 0
            for col in range(WIDTH):
                if(board[col][row] == -1):
                    bingo+=1
            if(bingo == HEIGHT):
                return True
    return False

def remainSum(board):
    sum = 0
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if(board[row][col] >= 0):
                sum += board[row][col]
    return sum

def test1(fnum):
    
    lines = fnum.readlines()
    bingoCards = []
    print(lines[0].rstrip().split(','))
    winningNum = list(map(int, lines[0].rstrip().split(',')))

    for i in range(2, len(lines), HEIGHT+1):
        newCard = []
        for j in range(0, HEIGHT):
            if(len(lines[i+j]) > 3):
                newLine = []
                for k in range(0, WIDTH*3, 3):
                    line = lines[i+j][k:k+2]
                    newLine.append(int(line))
                newCard.append(newLine)
        print(newCard)
        bingoCards.append(newCard)
    
    for newNum in winningNum:
        winner = []
        for card in bingoCards:
            if(bingo(card, newNum)):
                print(newNum)
                print(remainSum(card))
                print(card)
                return remainSum(card) * newNum
    #print(bingoCards)
    return 0


file=open("test.txt", 'r')
print("Test1: " + str(test1(file)))
file.close()

def removeCard(bingoCards, newNum, startIndex):
    for i in range(startIndex, len(bingoCards)):
        if(bingo(bingoCards[i], newNum)):
            return i
    return -1

def test2(fnum):
    
    lines = fnum.readlines()
    bingoCards = []
    print(lines[0].rstrip().split(','))
    winningNum = list(map(int, lines[0].rstrip().split(',')))

    for i in range(2, len(lines), HEIGHT+1):
        newCard = []
        for j in range(0, HEIGHT):
            if(len(lines[i+j]) > 3):
                newLine = []
                for k in range(0, WIDTH*3, 3):
                    line = lines[i+j][k:k+2]
                    newLine.append(int(line))
                newCard.append(newLine)
        #print(newCard)
        bingoCards.append(newCard)
    
    for newNum in winningNum:
        if(len(bingoCards) == 1):
            print(remainSum(bingoCards[0])*newNum)
            bingo(bingoCards[0], newNum)
            print(newNum)
            print(remainSum(bingoCards[0]))
            print(bingoCards[0])
            return remainSum(bingoCards[0]) * newNum   
        remove = removeCard(bingoCards, newNum, 0)
        while(remove >= 0):
            #print(remove)
            bingoCards.pop(remove)
            remove = removeCard(bingoCards, newNum, remove-1)    
        
        if(len(bingoCards) < 5):
            print(newNum)
            for card in bingoCards:
                print(remainSum(card) * newNum)
                print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in card]))
        print('-----------------')
    #print(bingoCards)
    return 0

file=open("testSub.txt", 'r')
print("Test 2: " + str( test2(file)))
file.close()

