productList = []
palindromeList = []
x = 100
finalNum = 0
while x < 999:
    v = 100
    while v < 999:
        product = v * x
        productList.append(product)
        v+=1
    x+=1
for item in productList:
    tempStr = str(item)
    lenStr = len(tempStr)
    revLenStr = lenStr - 1
    tempList1 = []
    tempList2 = []
    for x in range(lenStr):
        tempList1.append(tempStr[x])
        tempList2.append(tempStr[revLenStr - x])
    if tempList1 == tempList2:
        palindromeList.append(item)
for item in palindromeList:
    if item > finalNum:
        finalNum = item
print(finalNum)
