largestSeq = 0
largestX = 0
for x in range(1000000):
    z = 2
    y = x
    seqLen = 1
    while int(z) != 1:
        if z <= 1:
            break
        if y % 2 == 0:
            z = y/2
        else:
            z = 3*y + 1
        y = z
        seqLen += 1
    if (seqLen + 1) > largestSeq:
        largestSeq = seqLen + 1
        largestX = x
print('largest x chain value:', largestX)
