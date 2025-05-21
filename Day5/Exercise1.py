import math
n=int(input('Nhập số(Điều kiện số nguyên tố, đối xứng):'))
def check(n):
    check1=True
    check2=True
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            check1=False
            break
    strn=str(n)
    if strn!=strn[::-1]:
        check1=False
    print(check1,check2)
    return check1 * check2
while(check(n)==False):
    m=int(input('Không thỏa mãn yêu  cầu nhập lại'))
    n=m
print('n thỏa mãn')
