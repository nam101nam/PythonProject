# k=int(input("Nhập số lượng="))
a=[]
i=0
# while i<k:
#     n=input("Nhập tên: ")
#     g=int(input('Nhập điểm: '))
#     i+=1
#     a.append([n,g])
# print(a)
a=[['Nam',10],['Phuong',9],['Dung',1],['A',9],['B',9]]
b=[]
for i in a:
    if i[1] not in b:
        b.append(i[1])
b.sort()
b.reverse()
print(b)
count=0
name=[]
for i in a:
    if i[1]==b[1]:
        count+=1
        name.append(i[0])
name.sort()
if count>=2:
    print(name)