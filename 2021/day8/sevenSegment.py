

# find the numbers 1 4 7 and 8 in the input (not in order)
# count how many times these values are in ouput
def test1(fnum):
    lines = fnum.readlines()
    som = 0
    count = 0
    for line in lines:
        input, output = line.strip().split('|')
        digits = input.split(" ")
        display = output.strip().split(" ")
        for i in range(len(digits)):
            digits[i] = ''.join(sorted(digits[i]))
        for d in display:
            d_sorted = sorted(d.strip())
            if(not(len(d_sorted) == 5 or len(d_sorted) == 6)):
                count+=1
    print(count)
    return som

    


file=open("day8/test.txt", 'r')
print("Test1: " + str(test1(file)))
file.close()

def findOne(values):
    for v in values:
        if(len(v) == 2):
            values.remove(v)
            return v

def findTwo(values):
    for v in values:
        if(len(v) == 5):
            values.remove(v)
            return v

def findThree(values, one):
    almostZero = set(one)
    for v in values:
        if(len(v) == 5):
            if(len(almostZero | v) == 5):
                values.remove(v)
                return v

def findFour(values):
    for v in values:
        if(len(v) == 4):
            values.remove(v)
            return v

def findFive(values, nine):
    almostNine = set(nine) 
    for v in values:
        if(len(v) == 5):
            if(len(almostNine | v) == 6):
                values.remove(v)
                return v

def findSix(values):
    for v in values:
        if(len(v) == 6):
            values.remove(v)
            return v

def findSeven(values):
    for v in values:
        if(len(v) == 3):
            values.remove(v)
            return v

def findEight(values):
    for v in values:
        if(len(v) == 7):
            values.remove(v)
            return v

def findNine(values, four, seven):
    almostNine = set(four) | set(seven)
    for v in values:
        if(len(v) == 6):
            if(len(almostNine | v) == 6):
                values.remove(v)
                return v

def findZero(values, one):
    almostZero = set(one)
    for v in values:
        if(len(v) == 6):
            if(len(almostZero | v) == 6):
                values.remove(v)
                return v


# find the numbers 1 4 7 and 8 in the input (not in order)
# count how many times these values are in ouput
def test2(fnum):
    lines = fnum.readlines()
    som = 0
    count = 0
    for line in lines:
        input, output = line.strip().split('|')
        digits = input.split(" ")
        display = output.strip().split(" ")
        for d in range(len(display)):
            display[d] = set(sorted(display[d]))
        for i in range(len(digits)):
            digits[i] = set(sorted(digits[i]))

        mapping = [{} for i in range(11)]
        mapping[1] = findOne(digits)
        mapping[4] = findFour(digits)
        mapping[7] = findSeven(digits)
        mapping[8] = findEight(digits)

        #if condition ok => 9
        mapping[9] = findNine(digits, mapping[4], mapping[7])
        #elif condition ok => 0
        mapping[0] = findZero(digits, mapping[1])
        #else 6
        mapping[6] = findSix(digits)

        mapping[3] = findThree(digits, mapping[1])
        mapping[5] = findFive(digits, mapping[9])
        mapping[2] = findTwo(digits)
        result = 0

        for d in display:
            result = mapping.index(d) + (result *10)
        print(result)
        som+= result
    print(count)
    return som


file=open("day8/test.txt", 'r')
print("Test 2: " + str(test2(file)))
file.close()

