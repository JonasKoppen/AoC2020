
def day1(fnum):
    increaseCount = 0
    oldNum = 9999999
    lines = fnum.readlines()
    for line in lines:
        if(line.strip().isnumeric()):
            newNum = int(line)
            if(newNum > oldNum):
                increaseCount=increaseCount + 1
            oldNum = newNum
    return increaseCount


file=open("test.txt", 'r')
print("Test1: " + str(day1(file)))
file.close()

def test2(fnum, sumcount):
    windowIndex = 0
    sumWindow = [0 for i in range(sumcount)]
    increaseCount = 0
    old = 0
    lines = fnum.readlines()
    numlins = [int(i.strip()) for i in lines]
    for i in range(len(lines) - sumcount):
        new = sum(numlins[i: i + sumcount])
        if(new > old):
            increaseCount=increaseCount + 1
        old = new
    return increaseCount


file=open("test.txt", 'r')
print("Test 2: " + str( test2(file, 3)))
file.close()

