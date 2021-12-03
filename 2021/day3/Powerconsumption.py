
def test1(fnum):
    depth = 0
    forward = 0
    lines = fnum.readlines()
    bitmap = []
    
    for line in lines:
        bitmap.append(list(line.strip()))
    colSize = len(bitmap[0])
    gamma = 0b0
    theta = 0b0
    for i in range(colSize):
        one = 0
        zero = 0
        for j in range(len(bitmap)):
            if(bitmap[j][i] == '1'):
                one = one + 1
            elif(bitmap[j][i] == '0'):
                zero = zero + 1
        if(zero < one):
            gamma = (gamma<<1) | 0b1
            theta = (theta<<1) | 0b0
        else:
            gamma = (gamma<<1) | 0b0
            theta = (theta<<1) | 0b1
        print("gamma")
        print(gamma)
        print("theta")
        print(theta)
            

    return gamma * theta


file=open("test.txt", 'r')
print("Test1: " + str(test1(file)))
file.close()

def test2(fnum):
    depth = 0
    aim = 0
    forward = 0
    lines = fnum.readlines()
    for line in lines:
        command, change = line.strip().split(" ",1)
        if(command == "forward"):
            forward = forward + int(change)
            depth = depth + (aim * int(change))
        elif(command == "down"):
            aim = aim + int(change)
        elif(command == "up"):
            aim = aim - int(change)
        elif(command == "back"):
            forward = forward + int(change)
    print(str(depth) + ',' + str(forward))
    return depth * forward



file=open("test.txt", 'r')
#print("Test 2: " + str( test2(file)))
file.close()

