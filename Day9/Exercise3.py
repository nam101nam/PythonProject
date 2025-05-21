def tinh_tong(a,b):
    if isinstance(a,int) and isinstance(b,int):
        print('a,b là số nguyên')
        return a+b
    else:
        print('a, b phải là số nguyên')

print(tinh_tong(10,11))