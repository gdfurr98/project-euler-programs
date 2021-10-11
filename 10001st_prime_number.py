inputNum = input('What prime do you want? ')
inputNum = int(inputNum)
numList = []
x = 2
count = 2
while x > -1:
    if x != count:
        if x % count == 0:
            count = 2
            x+=1
            continue
    if x == count:
        numList.append(x)
        count = 2
        x+=1
        continue
    count+=1
    if len(numList) == inputNum:
        break
print(numList[inputNum-1])
