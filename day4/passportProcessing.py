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
    allowed = ["byr", "iyr", "eyr", "hgt", "ecl", "pid", "hcl"]
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
            if key in allowed:
                validCheck += 1
        if validCheck == 7:
            validPassCount += 1


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
                if (value.isdigit()) and (1920<=int(value)<=2002):
                    validCheck+=1
            elif "iyr" == key:
                if (value.isdigit()) and (2010<=int(value)<=2020):
                    validCheck+=1
            elif "eyr" == key:
                if (value.isdigit()) and (2020<=int(value)<=2030):
                    validCheck+=1
            elif "hgt" == key:
                h = value[:-2]
                t = value[-2:]
                if h.isdigit():
                    if t == "cm" and (150 <= int(h) <= 193):
                        validCheck+=1
                    elif t == "in" and (59 <= int(h) <= 76):
                        validCheck += 1
            elif "hcl" == key:
                if (value[0] == "#") and (len(value) == 7) and re.match(r"#([a-f|0-9]){6}", value) != None:
                    validCheck+=1
            elif "ecl" == key:
                if value in allowedEyes: #hack might need to check
                    validCheck+=1
            elif "pid" == key:
                if (len(value) == 9 and value.isdigit()):
                    validCheck+=1

        if validCheck == 7:
            validPassCount += 1


fname = "real.txt"
print(part1(fname))
print(part2(fname))
