

def ageFish(fish, fishToAdd):
    fish -= 1
    if(fish < 0):
        fish = 6
        fishToAdd+=1
    return fish, fishToAdd

def test1(fnum, simulateEnd):
    lines = fnum.readlines()
    fishList = list(map(int,lines[0].split(',')))
    fishies = [0 for i in range(10)] #pos 9 => -1
    for fish in fishList:
        fishies[fish] += 1
    print(fishies)
    for day in range(simulateEnd):
        for i in range(0,9):
            fishies[i-1] = fishies[i]
        fishies[8] = fishies[-1]
        fishies[6] += fishies[-1]
        print(day)
    fishies[-1] = 0
    print(len(fishies))
    return sum(fishies)
    


file=open("day6/dummy.txt", 'r')
print("Test1: " + str(test1(file, 80)))
file.close()



file=open("day6/test.txt", 'r')
print("Test 2: " + str(test1(file, 256)))
file.close()

