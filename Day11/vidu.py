# class SinhVien:
#     def __init__(self,masv,ten):
#         self.masv=masv
#         self.ten=ten
#     def gioi_thieu(self):
#         print('Tôi tên là:',self.ten,' và mã sinh viên:',self.masv)
# sinhvien=SinhVien(1001,'Đỗ Phương Nam')
# sinhvien.gioi_thieu()

# class HinhChuNhat:
#     def __init__(self,chieudai,chieurong):
#         self.chieudai=chieudai
#         self.chieurong=chieurong
#     def chu_vi(self):
#         return (self.chieudai+self.chieurong)*2
#     def dien_tich(self):
#         return self.chieudai*self.chieurong
# hinh1=HinhChuNhat(2,5)
# print('Chu vi hình chữ nhật:',hinh1.chu_vi())
# print('Diện tích hình chữ nhật:',hinh1.dien_tich())

# class DongVat:
#     def __init__(self,ten):
#         self.ten=ten
#     def keu(self):
#         print('Con vat keu')
# class Cho(DongVat):
#     def keu(self):
#         print(self.ten,'kêu gâu gâu')
# cho1=Cho('Bunny')
# cho1.keu()
# dongvat=DongVat('Kitty')
# dongvat.keu()

# class Meo:
#     def keu(self):
#         print("Meo meo")
#
# class Cho:
#     def keu(self):
#         print("Gâu gâu")
#
# # Dùng đa hình
# def lam_con_vat_keu(convat):
#     convat.keu()
#
# lam_con_vat_keu(Meo())  # → Meo meo
# lam_con_vat_keu(Cho())  # → Gâu gâu

# class PhanSo:
#     def __init__(self,tuso,mauso):
#         self.tuso=tuso
#         self.mauso=mauso
#     def __str__(self):
#         return str(self.tuso/self.mauso)
#     def tuso.__add__(mauso):
#
# a=PhanSo(10,3)
# print(a)

