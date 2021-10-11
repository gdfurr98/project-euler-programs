from sympy import factorint
finalNum = 0
x = factorint(600851475143)
for z in x:
    if z > finalNum:
        finalNum = z
print(finalNum)
