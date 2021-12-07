

def ageFish(fish, fishToAdd):
    fish -= 1
    if(fish < 0):
        fish = 6
        fishToAdd+=1
    return fish, fishToAdd

def test1(fnum, simulateEnd):
    lines = fnum.readlines()
    fishList = list(map(int,lines[0].split(',')))
    for day in range(simulateEnd):
        fishToAdd = 0
        for i in range(len(fishList)):
            fishList[i], fishToAdd = ageFish(fishList[i], fishToAdd)
        if(fishToAdd > 0):
            for i in range(fishToAdd):
                fishList.append(8)
        print(day)
    print(len(fishList))
    return len(fishList)
    


file=open("test.txt", 'r')
print("Test1: " + str(test1(file, 80)))
file.close()



file=open("test.txt", 'r')
print("Test 2: " + str(test1(file, 256)))
file.close()

