import re
from operator import xor


# not 60 not 71

def readGroup(file):
    group = ""
    while True:
        line = file.readline()
        if line.rstrip() == '':
            return group
        group += line


def part1(fname):
    file = open(fname, "r")
    yesCount = 0
    while True:
        group = readGroup(file).replace("/n", "").rstrip().lower()
        yesList = [0 for _ in range(26)]
        if group == "eof":
            file.close()
            return yesCount
        for g in group:
            if g.isalpha():
                yesList[ord(g)-97] = 1
        yesCount += sum(yesList)
        print(yesCount)
        print(yesList)

def part2(fname):
    file = open(fname, "r")
    yesCount = 0

    while True:
        group = readGroup(file).lower()
        yesList = [0 for _ in range(26)]
        personCount = 0
        if group == "eof":
            file.close()
            return yesCount
        entry = group.split("\n")
        for e in entry:
            if e != '':
                personCount += 1
                for g in e:
                    if g.isalpha():
                        yesList[ord(g)-97] += 1
        for i in yesList:
            if(i>0):
                if(i==personCount):
                    yesCount+=1
        print(personCount)
        print(yesCount)
        print(yesList)


fname = "real.txt"
print(part1(fname))
print(part2(fname))
