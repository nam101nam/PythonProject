n=int(input('Nhập n='))
count=0
while n!=1:
    count+=1
    if(n%2==0):
        n/=2
        continue
    else:
        n=n*3+1
print('Số bước:',count)