# so_thanh_vien=int(input('Nhập số thành viên:'))
# i=0
list=['SV01 Minh Nam 9.5',
'SV02 Nam Nam 9.1',
'SV03 Linh Nu 9.2',
'SV04 Long Nam 9.8',
'SV05 Nga Nu 8.8']
# while i <so_thanh_vien:
#     string=input('Nhập thông tin(gồm Mã Sinh Viên, Họ Tên, Giới tính, Điểm:)')
#     list.append(string)
#     i+=1
newlist=[]
for i in list:
    newlist.append(i.split())
newlistsort=sorted(newlist,key=lambda x:x[3],reverse=True)
for i in range(0,3,1):
    toString=' '.join(newlistsort[i])
    print(toString)