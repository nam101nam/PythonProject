# so_chuoi=int(input('Nhập số chuỗi cần kiểm tra: '))
list=['aaaaaaaaa', 'a1b1b3', 'aaasss1@123']
# i=0
# while i<so_chuoi:
#     string=input('Nhập chuỗi:')
#     list.append(string)
#     i+=1
count=0
for a in list:
    if len(a)<6:
        continue
    checkusn=False
    checkpha=False
    checkdi=False
    for b in a:
        if b.isdigit():
            checkdi=True
        if b.isalpha():
            checkpha=True
        if not b.isalnum():
            checkusn=True
            break
    print(checkusn,checkpha,checkdi)
    if  checkusn==False and checkdi==True and checkpha==True:
        count+=1
print(count)