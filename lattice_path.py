import math
gridLen = input('What is the length of our grid?')
gridLen = int(gridLen)+1
print("The factorial of the length is:", math.factorial(int(gridLen)))
numPathDenom = math.factorial((2*(gridLen-1)))
numPathNumerat = math.factorial(gridLen-1)**2
print(numPathDenom/numPathNumerat)
