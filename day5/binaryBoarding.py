import re
from operator import xor


# not 60 not 71

def readPass(file):
    passport = ""
    while True:
        line = file.readline()
        if len(line) < 2:
            return passport
        passport += line


def part1(fname):
    file = open(fname, "r")
    highestSeat = -1
    seatList = []
    while True:
        passport = file.readline()
        if(len(passport) < 4):
            seatList.sort()
            for i in range(seatList[0], seatList[-1]):
                if(seatList[0] + i != seatList[i]):
                        file.close()
                        return seatList[0] + i
            file.close()
            return seatList[0] + i
        row = 0b000000
        column = 0b000
        for b in passport:
            if (b == "F" or b == "B"):
                row = (row<<1) | 0x1 * bool(b == "B")
            elif (b == "L" or b == "R"):
                column = (column<<1) | 0x1 * bool(b == "R")
        print(int(row))
        print(int(column))
        seatId = int(row) * 8 + int(column)
        seatList.append(seatId)


def part2(fname):
    file = open(fname, "r")
    allowedEyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    validPassCount = 0

    while True:
        passport = readPass(file)
        if "EOF" in passport:
            file.close()
            return validPassCount
        passfields = passport.rstrip().replace("\n", " ").split(" ")
        validCheck = 0
        for f in passfields:
            key, value = f.split(":", 1)
            if "byr" == key:
                if (value.isdigit()) and (1920 <= int(value) <= 2002):
                    validCheck += 1
            elif "iyr" == key:
                if (value.isdigit()) and (2010 <= int(value) <= 2020):
                    validCheck += 1
            elif "eyr" == key:
                if (value.isdigit()) and (2020 <= int(value) <= 2030):
                    validCheck += 1
            elif "hgt" == key:
                h = value[:-2]
                t = value[-2:]
                if h.isdigit():
                    if t == "cm" and (150 <= int(h) <= 193):
                        validCheck += 1
                    elif t == "in" and (59 <= int(h) <= 76):
                        validCheck += 1
            elif "hcl" == key:
                if (value[0] == "#") and (len(value) == 7) and re.match(r"#([a-f|0-9]){6}", value) != None:
                    validCheck += 1
            elif "ecl" == key:
                if value in allowedEyes:  # hack might need to check
                    validCheck += 1
            elif "pid" == key:
                if (len(value) == 9 and value.isdigit()):
                    validCheck += 1

        if validCheck == 7:
            validPassCount += 1


fname = "real.txt"
print(part1(fname))
#print(part2(fname))
