a=int(input('Nhap a='))
b=int(input('Nhap b='))
if a>b:
    print('a be hon hoac ')
else:
    c=0
    for i in range(a,b+1,1):
        if i%2 !=0: c=c+i

print(c)