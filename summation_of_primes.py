import math
sum = 0
for x in range(2, 2000000):
    bool = False
    for y in range(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            bool = True
            break
    if bool == False:
        sum+=x
print(sum)
