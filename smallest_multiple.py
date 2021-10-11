inputNum = input('Number: ')
inputNum = int(inputNum)
numList = []
x = 1
z = 1
counter = 0
while z <= inputNum:
    numList.append(z)
    z+=1
print(numList)
while x > -1:
    if x % numList[counter] != 0:
        counter = 0
        x += 1
        continue
    counter+=1
    if counter == len(numList):
        break
print(x)
