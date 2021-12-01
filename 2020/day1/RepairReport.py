
def day1(fnum):
    numlist = []

    newnum = int(fnum.readline())
    numlist.append(newnum)
    while fnum:
        newnum = int(fnum.readline())
        for n in numlist:
            if n + newnum == 2020:
                return n * newnum
        numlist.append(newnum)
    return  -1


file=open("test.txt", 'r')
print(day1(file))
file.close()

