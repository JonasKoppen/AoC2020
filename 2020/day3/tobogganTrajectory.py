from operator import xor
#not 60 not 71

def part1(fname):

    stepx = 3
    stepy = 1
    posx = -3
    posy = 0
    treeCount = 0
    file = open(fname, 'r')

    while file:
        line = file.readline()
        if line == '':
            file.close()
            break

        line = line.strip().rstrip()
        width = len(line)
        posx += stepx

        if line[posx % width] == "#":
            treeCount += 1
        #print(line)
        pos = "X" if (line[posx % width] == '#') else "0"
        print(line[:posx % width] + pos +line[(posx % width)+1:])
    return treeCount


def part2(fname, stepx, stepy):
    posx = -stepx
    posy = 0
    treeCount = 0
    file = open(fname, 'r')

    while file:
        line = file.readline()
        if line == '':
            file.close()
            break


        line = line.strip().rstrip()
        width = len(line)
        posx += stepx

        if line[posx % width] == "#":
            treeCount += 1
        #print(line)
        #pos = "X" if (line[posx % width] == '#') else "0"
        #print(line[:posx % width] + pos +line[(posx % width)+1:])
        if (stepy == 2):
            line = file.readline()
            if line == '':
                file.close()
                break
    return treeCount


fname = "real.txt"
print(part1(fname))
print(part2(fname,1,1))
print(part2(fname,3,1))
print(part2(fname,5,1))
print(part2(fname,7,1))
print(part2(fname,1,2))
