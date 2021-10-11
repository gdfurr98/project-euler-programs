inputNum = input("Number: ")
numList = []
z = 0
numSum = 0
sumOSquares = 0
while z <= int(inputNum):
    numList.append(z)
    z+=1
for x in numList:
    square = x ** 2
    sumOSquares += square
    numSum += x
squareNumSum = numSum ** 2
print(numList)
print(squareNumSum)
print(sumOSquares)
print(squareNumSum - sumOSquares)
