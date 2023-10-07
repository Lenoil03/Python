from phan_so import PhanSo
class DanhSachPs:
    def __init__(self) -> None:
        self.ds = []

    def them(self, ps: PhanSo):
        self.ds.append(ps)

    def xuat(self):
        for ps in self.ds:
            print(ps, end = " ")
        print()

    def docTuFile(self, tenFile):
        with open(tenFile, "r", encoding = "utf-8") as f:
            for hang in f:
                du_lieu = hang.split("/")
                ps = PhanSo(int(du_lieu[0]), int(du_lieu[1]))
                self.ds.append(ps)
    def demPsAm(self):
        dem = 0
        for ps in self.ds:
            if ps.laPsAm():
                dem += 1
        return dem

    def layDsPsAm(self):
        dsAm = DanhSachPs()
        for ps in self.ds:
            if ps.laPsAm():
                dsAm.them(ps)
        return dsAm

    def layDsPsDuong(self):
        dsDuong = DanhSachPs()
        for ps in self.ds:
            if not ps.laPsAm():
                dsDuong.them(ps)
        return dsDuong