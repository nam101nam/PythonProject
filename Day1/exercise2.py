print('Chao mung den LabAI HaUI')
print('Khoa CNTT thuoc truong DH Cong nghiep Ha Noi - “10 diem”')
s='Khoa CNTT thuoc truong DH Cong nghiep Ha Noi'
s1=''
s2=''
s3=''
s=s.replace(' ','')
for i in s:
    if i==i.upper():
        s1+=i
    elif i==i.lower():
        s2+=i

print('Chuoi hoa:',s1)
print('Chuoi thuong:',s2)

if s.find('CNTT',0)!= -1:
    print('Yes')
else:
    print('No')
for i in s:
    if i==i.upper():
        s3+=i.lower()
    elif i==i.lower():
        s3+=i.upper()
print(s3)

