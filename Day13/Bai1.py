import random
def nhapSo():
    n = int(input("Enter a number: "))
    return n
def check(n):
    rando = random.randint(1, 100)
    print('Số chính xác:',rando)
    if(rando == n):
        print('Bạn đã đoán đúng! Xin chúc mừng!!')
    elif(rando < n):
        print('oppp!! Số bạn nhập lớn hơn mất rùi!!')
    else:
        print('Số bạn nhập nhỏ hơn số cần đoán rùi!!!')
n=nhapSo()
check(n)
