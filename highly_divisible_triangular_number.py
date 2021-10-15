from math import sqrt
def divisorCheck(number):
    y = 2
    d = 2
    while y <= sqrt(number):
        if number % y == 0:
            d+=1
            if y != number / y:
                d+=1
        y+=1
    return d
count = 2
z = 0
while z < 500:
    number = 0
    for x in range(count):
        number+=x
    z = divisorCheck(number)
    count+=1
print("number:", number, "divisors:", z)
