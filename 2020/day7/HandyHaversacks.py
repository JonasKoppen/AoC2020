import re
from operator import xor


# bag list [parent colour, chile1 colour, child2 colour, ..., child2 colour]

# parent colour = colour without bag
# child is allowd to have the word bag

def prepareCondition(fname):
    file = open(fname, "r")
    conditions = []
    while True:
        line = file.readline()
        if line.rstrip() == '':
            file.close()
            return conditions
        parent, allChildren = line.split("contain", 1)
        parent, _ = parent.split("bag")
        clist = allChildren.rstrip().replace(".", "").split(",")
        clist.insert(0, parent.rstrip())
        conditions.append(clist)


def recursivePart(validColours, conditions):
    prelenght = len(validColours)
    newValids = validColours.copy()
    for cList in conditions:
        if not cList[0] in validColours:
            for c in cList[1:]:
                for vc in validColours:
                    if vc in c:
                        colour = cList[0]
                        newValids.append(colour)
    if prelenght == len(newValids):
        print(list( dict.fromkeys(validColours) ))
        return len(list( dict.fromkeys(validColours) ))
    else:
        return recursivePart(newValids, conditions)


def part1(fname):
    conditions = prepareCondition(fname)
    return recursivePart(["shiny gold"], conditions)

def recursivePart2(validColours, conditions, currentColour):
    bagCount = 0
    for cList in conditions:
        if cList[0] == currentColour:
            if("no other" in cList[1]):
                return 0
            for c in cList[1:]:
                cc = c[2:]
                cc, _ = cc.split(" bag")
                cc = cc.strip(" ")
                #print(cc)
                #print(int(c[1]))
                bagCount += int(c[1]) * recursivePart2(validColours, conditions, cc)
                bagCount += int(c[1])
    print("bagcount for colour:")
    print(currentColour)
    print(bagCount)
    return bagCount

def part2(fname):
    conditions = prepareCondition(fname)
    return recursivePart2(["shiny gold"], conditions, "shiny gold")


colourList = []
fname = "real.txt"
print(prepareCondition(fname))
print("part1:")
print(part1(fname))
print("part2:")
print(part2(fname))
