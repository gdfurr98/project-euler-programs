a = 1
b = 1
c = 1
m = 2
n = 1
z = 1
while z != 1000:
    a = m**2-n**2
    b = 2*m*n
    c = m**2+n**2
    z = a + b + c
    if z > 1000:
        n+=1
        m=2
    print("z:",z,"a:",a,"b:",b,"c:",c,"n:",n,"m:",m)
    m+=1
print(a*b*c)
