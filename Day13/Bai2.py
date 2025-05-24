import random
aliens=2
print('So luong nguoi ngoai hanh tinh=',aliens)
n=(input('Nhap mat khau gom 6 chu so:'))
password=f"{random.randint(0, 999999):06d}"
while(password!=n):
    aliens**=2
    print('So luong nguoi ngoai hanh tinh=', aliens)
    if(aliens>8000000000):
        print('So aliens vuot qua 8 ti nguoi! Game over!')
        break
    n =(input('Nhap lai mat khau:'))
else:
    print('Mo kho vu khi thanh cong! You are hero!')
print('Mat khau kho vu khi la:',password)
