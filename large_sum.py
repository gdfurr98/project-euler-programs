fhand = open('large_sum13.txt')
numSum = 0
for line in fhand:
    numSum+=int(line.strip())
print(numSum)
