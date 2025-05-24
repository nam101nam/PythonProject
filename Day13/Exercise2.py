n=input('Nhập số:')
def kiem_tra_doi_xung(n,a,b):
    loi=0
    while a>0 and b<len(n):
        if n[a]!=n[b]:
            loi+=1
            print(f'Vi tri loi {a} khac {b}, {n[a]} khac {n[b]}')
            n = list(n)
            n[a] = n[b]
            n = ''.join(n)
        a-=1
        b+=1
    tong_hop=[loi,n]
    return tong_hop
if(len(n)%2==0):
    print('So loi va chuoi sau khi xua:',kiem_tra_doi_xung(n, int(len(n)/2)-1,int(len(n)/2)))
else:
    print('So loi va chuoi sau khi sua',kiem_tra_doi_xung(n, int(len(n)/2),int(len(n)/2)))