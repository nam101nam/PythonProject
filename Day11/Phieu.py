class PhieuNhap:
    a=[]
    tong=0
    def __init__(self,maphieu,manhacc,diachi,ngaylap,tennhacc):
        self.maphieu = maphieu
        self.manhacc = manhacc
        self.diachi = diachi
        self.ngaylap = ngaylap
        self.tennhacc = tennhacc
    def hienThi(self):
        print('_' * 60)
        print(f'{'PHIẾU NHẬP HÀNG':^60}')
        print(f'Mã phiếu:{self.maphieu:<25}Ngày lập:{self.ngaylap}')
        print(f'Mã NCC:{self.manhacc:<27}Tên NCC:{self.tennhacc}')
        print('Địa chỉ:',self.diachi)
        print('_'*60)
        print(f'{'Tên hàng:':<15}{'Đơn giá:':<15}{'Số lượng:':<15}{'Thành tiền:':<15}')
        for h in PhieuNhap.a:
            print(f'{h.tenhang:<15}{h.dongia:<15}{h.soluong:<15}{h.dongia*h.soluong:<15.2f}')
            PhieuNhap.tong+=h.dongia*h.soluong
        print(f'{'':<25}{'Cộng thành tiền':<20}{PhieuNhap.tong}')
        print('_' * 60)
class MatHang:
    def __init__(self,tenhang,dongia,soluong):
        self.tenhang = tenhang
        self.dongia = dongia
        self.soluong = soluong
        PhieuNhap.a.append(self)

