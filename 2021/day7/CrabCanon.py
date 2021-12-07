
def fuelSum(crablist, x):
    fuelCost = 0
    for crab in crablist:
        dist = abs(crab - x)
        fuelCost += (dist*(dist+1))/2
    return fuelCost

def findLowest(crablist, x, rico):
    r0 = fuelSum(crablist, x)
    r1 = fuelSum(crablist, x + rico)
    if(r0 > r1):
        return findLowest(crablist, x+rico, rico)
    print("pos: "+str(x) +" with points: " + str(r0))
    return r0

#find median (creates test 2 in test 1)

def test2(fnum):
    lines = fnum.readlines()
    crablist = list(map(int,lines[0].split(',')))
    crablist.sort()
    print(crablist)
    fuelCost = 0
    x = crablist[int(len(crablist)/2)]
    r0 = fuelSum(crablist, x-1)
    r1 = fuelSum(crablist, x)
    r2 = fuelSum(crablist, x+1)
    if(r0 < r1):
        rico = -1
    elif(r1 > r2):
        rico = 1
    else:
        return r1
    print(r0)
    print(x)
    return findLowest(crablist, x, rico)


    


file=open("day7/dummy.txt", 'r')
#print("Test1: " + str(test1(file)))
file.close()



file=open("day7/test.txt", 'r')
print("Test 2: " + str(test2(file)))
file.close()

