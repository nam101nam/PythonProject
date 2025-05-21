import random
so_thanh_vien=int(input('Nhập số thành viên'))
edu_mail={
}
for i in range(1,so_thanh_vien+1,1):

    username=input('Nhập tài khoản(10 ký tự là mã sinh viên):')
    while len(username)!=10:
        username = input('Nhập  lại tài khoản(10 ký tự là mã sinh viên):')
    username1=username+'@lab601.edu.vn'
    password=input('Nhập mật khẩu:')
    number = random.randint(0, 999)
    number1 = str(number).zfill(3)
    password1=number1+password
    edu_mail[username1]={'mail':username1,'password':password1}
print(edu_mail)