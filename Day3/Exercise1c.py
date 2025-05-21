import math
n=int(input('Nhap n= '))
i=2
s=0
while i<=n:
    j=2
    a=True
    while j<=int(math.sqrt(i)):
        if i%j==0:
            a=False
            break
        j+=1
    if a==True:
        s+=i
    i+=1
print(s)