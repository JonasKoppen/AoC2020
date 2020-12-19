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
        action, count = line.split(" ", 1)
        count = int(count)
        conditions.append([action, count])


def part1(fname):
    currentLine = 0
    usedLines = []
    acc = 0
    conditions = prepareCondition(fname)
    while True:
        if currentLine in usedLines:
            return acc
        usedLines.append(currentLine)
        if(conditions[currentLine][0] == "nop"):
            currentLine+=1
        elif(conditions[currentLine][0] == "acc"):
            acc+=conditions[currentLine][1]
            currentLine += 1
        elif (conditions[currentLine][0] == "jmp"):
            currentLine+=conditions[currentLine][1]

def part2Verify(conditions):
    currentLine = 0
    usedLines = []
    acc = 0
    while currentLine < len(conditions):
        if currentLine in usedLines:
            return 0
        usedLines.append(currentLine)
        if(conditions[currentLine][0] == "nop"):
            currentLine+=1
        elif(conditions[currentLine][0] == "acc"):
            acc+=conditions[currentLine][1]
            currentLine += 1
        elif (conditions[currentLine][0] == "jmp"):
            currentLine+=conditions[currentLine][1]
    return acc


def part2(fname):
    conditions = prepareCondition(fname)
    for i in range(len(conditions)):
        if conditions[i][0] == "jmp":
            con = conditions.copy()
            con[i] = ["nop", con[i][1]]
            result = part2Verify(con)
            if(result != 0):
                return result
        elif conditions[i][0] == "nop":
            con = conditions.copy()
            con[i] = ["jmp", con[i][1]]
            result = part2Verify(con)
            if(result != 0):
                return result


colourList = []
fname = "real.txt"
#print(prepareCondition(fname))
print("part1:")
print(part1(fname))
print("part2:")
print(part2(fname))
