from operator import xor


def part1(fnum):
    validcount = 0

    while fnum:
        line = fnum.readline()
        if line == '':
            break
        condition, entry = line.split(":", 1)
        low, condition = condition.split("-", 1)
        high, letter = condition.split(" ", 1)

        if int(low) <= entry.count(letter) <= int(high):
            validcount += 1

    return validcount

def part2(fnum):
    validcount = 0

    while fnum:
        line = fnum.readline()
        if line == '':
            break
        condition, entry = line.split(":", 1)
        low, condition = condition.split("-", 1)
        high, letter = condition.split(" ", 1)
        entry = entry.strip()
        isLow = entry[int(low)-1] == letter
        isHigh = entry[int(high)-1] == letter
        if (isLow != isHigh):
            validcount += 1

    return validcount


file = open("test.txt", 'r')
print(part1(file))
file.close()

file = open("real.txt", 'r')
print(part2(file))
file.close()

