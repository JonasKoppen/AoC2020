HEIGHT = 5
WIDTH = 5

"""
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
"""

def mapVentLine(diagram, ventline, noDiagonal):
    currentPos = ventline[0]
    desitanionPos = ventline[1]
    #print(currentPos)
    #print(desitanionPos)
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in diagram]))
    if(noDiagonal and currentPos[0] != desitanionPos[0] and currentPos[1] != desitanionPos[1]):
            return
    while(True):
        #diagram[Y][X]
        diagram[currentPos[1]][currentPos[0]] += 1
        if(currentPos[0] == desitanionPos[0] and currentPos[1] == desitanionPos[1]):
            return
        # update X
        if(currentPos[0] > desitanionPos[0]):
            currentPos[0]-=1
        elif(currentPos[0] < desitanionPos[0]):
            currentPos[0]+=1
        else:
            pass
        #update Y
        if(currentPos[1] > desitanionPos[1]):
            currentPos[1]-=1
        elif(currentPos[1] < desitanionPos[1]):
            currentPos[1]+=1
        else:
            pass

def test1(fnum):
    diagram = [[0]*1000 for i in range(1000)]
    ventlines = []
    lines = fnum.readlines()
    for line in lines:
        start, stop =  line.strip().split('->')
        ventlines.append([list(map(int,start.split(','))), list(map(int,stop.split(',')))])
    for ventline in ventlines:
        mapVentLine(diagram, ventline, True)
    dangerCount = 0;
    for line in diagram:
        for point in line:
            if(point >= 2):
                dangerCount+=1
    #print(ventlines)
    return dangerCount


file=open("test.txt", 'r')
print("Test1: " + str(test1(file)))
file.close()


def test2(fnum):
    diagram = [[0]*1000 for i in range(1000)]
    ventlines = []
    lines = fnum.readlines()
    for line in lines:
        start, stop =  line.strip().split('->')
        ventlines.append([list(map(int,start.split(','))), list(map(int,stop.split(',')))])
    for ventline in ventlines:
        mapVentLine(diagram, ventline, False)
    dangerCount = 0;
    for line in diagram:
        for point in line:
            if(point >= 2):
                dangerCount+=1
    #print(ventlines)
    return dangerCount

file=open("test.txt", 'r')
print("Test 2: " + str( test2(file)))
file.close()

