
def test1(fnum):
    depth = 0
    forward = 0
    lines = fnum.readlines()
    for line in lines:
        command, change = line.strip().split(" ",1)
        if(command == "forward"):
            forward = forward + int(change)
        elif(command == "down"):
            depth = depth + int(change)
        elif(command == "up"):
            depth = depth - int(change)
        elif(command == "back"):
            forward = forward + int(change)
    print(str(depth) + ',' + str(forward))
    return depth * forward


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
print("Test 2: " + str( test2(file)))
file.close()

