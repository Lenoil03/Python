from datetime import datetime
class SinhVien:
    truong = "Dai hoc Da Lat"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

        @maSo.setter
        def maSo(self, maso):
            if self.laMaSoHopLe(maso):
                self.__maSo = maso
    @staticmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
An = SinhVien("1", "An", 12)
print(An)
print(An.truong)
An.doiTenTruong(An, "Da Lat")
print(An.truong)
An.__str__()
An.xuat()