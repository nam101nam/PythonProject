n=int(input('Nhập số thành viên trong lab: '))
i=0
name=[]
age=[]
gioitinh=[]
honnhan=[]
while i<n:
    name1=input('Nhập học và tên người thứ '+str(i+1)+': ')
    name.append(name1)
    age1=input('Nhập tuổi: ')
    age.append(age1)
    gioitinh1=input('Nhập giới tính: ')
    gioitinh.append(gSioitinh1)
    honnhan1=input('Đã kết hôn hay chưa? Rồi/Chưa: ')
    honnhan.append(honnhan1)
    i+=1
j=0
print('******************************')
while j<n:
    print('Ho va ten: '+name[j])
    print('Nhap tuoi: ' + age[j])
    print('Nhap gioi tinh: ' + gioitinh[j])
    print('Da ket hon?: ' + honnhan[j])
    print('******************************')
    j+=1