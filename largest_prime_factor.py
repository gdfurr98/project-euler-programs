from sympy import factorint
factorList = []
finalNum = 0
x = factorint(600851475143)
for z in x:
    factorList.append(z)
for y in factorList:
    if y > finalNum:
        finalNum = y
print(finalNum)
