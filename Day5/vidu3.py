a=(1,1, 2, 4, 2, 3, 9, 8, 1, 2, 5, 7)
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    if a.count(b[i])%3==0 and a.count(b[i])%9!=0:
        print(b[i],end=' ')