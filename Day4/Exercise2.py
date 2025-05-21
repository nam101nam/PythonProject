# n=int(input('Nhập n='))
list=[
'SV00 Lâm 10',
'SV01 Mạnh 3',
'SV02 Đào 3',
'SV03 Ngọc 2',
'SV04 Ánh 2',
'SV05 Hải 5'

]
n=6
# for i in range(n):
#     str=input('Nhập thông tin(Mã Sinh Viên, Tên, tần suất lên lab):')
#     list.append(str)
newlist=[]
for i in list:
    newlist.append(i.split())
newlistsort = sorted(newlist, key=lambda x: int(x[2]), reverse=True)

print(newlistsort)
print('Top vinh danh')
for i in newlistsort:
    if(int(i[2])==int(newlistsort[n-1][2])):
        print(i)