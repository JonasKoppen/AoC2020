

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



file=open("day8/test.txt", 'r')
#print("Test 2: " + str(test2(file)))
file.close()

