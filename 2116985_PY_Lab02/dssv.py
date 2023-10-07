from datetime import datetime
from sinh_vien import SinhVien
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.endwith(ten)]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

ds = DanhSachSv()
sv1 = SinhVien(1, "1", "1/1/1111")
sv2 = SinhVien(2, "2", "2/2/2222")
sv3 = SinhVien(3, "3", "3/3/3333")
sv4 = SinhVien(4, "4", "4/4/4444")
sv5 = SinhVien(5, "5", "5/5/5555")
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.xuat()
print(str(ds.timVTSvTheoMssv(3)))
print("Xoa thanh cong" if ds.xoaSvTheoMssv(4) else "Khong thanh cong")
ds.xuat()
print(ds.timSvTheoTen("3"))