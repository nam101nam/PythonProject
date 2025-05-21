a=input('Nhập mã bưu điện: ')
if(len(a)!=6 and a[0]!=0):
    print('Mã bưu điện không hợp lệ 1')
else:
    count=0;
    for i in range(len(a)-2):
        if(a[i]==a[i+2]):
            count+=1
    if(count>=2):
        print('Mã bưu điện không hợp lệ 2')
    else:
        print('Mã bưu điện hợp lệ')