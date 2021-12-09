

# find the numbers 1 4 7 and 8 in the input (not in order)
# count how many times these values are in ouput
def test1(fnum):
    lines = fnum.readlines()
    kaart = [[int(i) for i in line.strip()] for line in lines]
    #print(kaart)
    depths = 0

    for row in range(len(kaart)):
        for col in range(len(kaart[0])):
            depthcount = 0

            if(row == len(kaart)-1):
                depthcount+=1
            elif(kaart[row+1][col] > kaart[row][col]):
                depthcount+=1

            if(row == 0):
                depthcount+=1
            elif(kaart[row-1][col] > kaart[row][col]):
                depthcount+=1

            if(col == len(kaart[0])-1):
                depthcount+=1
            elif(kaart[row][col+1] > kaart[row][col]):
                depthcount+=1

            if(col == 0):
                depthcount+=1
            elif(kaart[row][col-1] > kaart[row][col]):
                depthcount+=1

            if(depthcount == 4):
                print("Depth:" + str(kaart[row][col]))
                depths+=kaart[row][col]+1
            

    return depths

    


file=open("day9/test.txt", 'r')
print("Test1: " + str(test1(file)))
file.close()




file=open("day9/test.txt", 'r')
#print("Test 2: " + str(test2(file)))
file.close()

