s=input('Nhập chuỗi s=')
t=input('Nhập chuỗi t=')
k=int(input('Nhập k='))
a=0
for i in range(0,min(len(s),len(t)),1):
    if(s[i]==t[i]):
        a+=1
    else:
        break
if((len(s)-a+len(t)-a)==k):
    print('Thỏa mãn')
else:
    print('Không thỏa mãn')
print((len(s)-a+len(t)-a))
print(a)