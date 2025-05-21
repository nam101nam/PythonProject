khachmoi=input("Khách hàng mới? (yes/no): ").strip().lower()
soluong=int(input("Nhập số lượng sản phẩm: "))
tong=float(input("Nhập tổng giá trị đơn hàng: "))
giam=0
if khachmoi=='yes'and soluong>10 and tong > 100000:
    giam+=20
else:
    if khachmoi=='yes':
        giam+=5
    else:
        giam+=10
    if 6<=soluong<=10:
        giam+=5
    elif soluong>10:
        giam+=10
    if 10000<=tong<=50000:
        giam+=8
    elif tong>50000:
        giam+=15
tong_sau_giam=tong*(1-giam/100)
print("Tổng giá trị cuối cùng của đơn hàng sau khi giảm giá:"+str(tong_sau_giam))
