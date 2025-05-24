from math import*
def tong_uoc(n):
    i=1
    s=0
    while(i<n):
        if(n%i==0):
            s+=i
        i+=1
    return s

def check_than_thiet(a0,a1):
    if(a0==tong_uoc(a1) and a1==tong_uoc(a0)):
        return True
    else:
        return False

def count_than_thiet(mang):
    mangtt = []
    thanthiet = 0
    for i in range(0, len(mang), 2):
        if check_than_thiet(int(mang[i]), int(mang[i + 1])) == True:
            mangtt.append(int(mang[i]))
            mangtt.append(int(mang[i + 1]))
            thanthiet += 1
    print('Co', thanthiet, 'cap than thiet')
    return mangtt

def count_hua_hon(mang):
    manghh=[]
    huahon=0
    for i in range(0, len(mang), 2):
        a=int(mang[i])
        b=int(mang[i + 1])

        if abs(tong_uoc(a) - b)==1 and abs(tong_uoc(b) - a)==1:
            manghh.append(tt[i])
            manghh.append(tt[i+1])
            huahon += 1
    print('Co', huahon, 'cap hua hon')

a=input('Nhap cap so:')
mang=a.split()
tt=count_than_thiet(mang)
count_hua_hon(mang)

