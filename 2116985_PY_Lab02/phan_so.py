import math
class PhanSo:
    def __init__(self, tuSo = 1, mauSo = 1) -> None:
        self.tu = tuSo
        self.mau = mauSo if mauSo != 0 else 1
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __add__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq

    def laPsAm(self):
        return self.tu * self.mau < 0