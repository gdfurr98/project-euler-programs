evenList = []
evenSum = 0
def fibonacci(a, b):
    print('a', a)
    print('b', b)
    if b % 2 == 0:
        evenList.append(b)
    if a >= 4000000:
        return
    else:
        newA = b
        newB = a + b
        fibonacci(newA, newB)
fibonacci(1, 2)
for x in evenList:
    evenSum += x
print(evenList)
print(evenSum)
