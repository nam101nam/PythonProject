n=int(input('Nhap n= '))
i=0
while i<n:
    i+=1
    if i%3==0:
        continue
    elif i%10==0:
        break
    else:
        print(i)
