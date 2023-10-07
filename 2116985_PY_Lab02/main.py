from phan_so import PhanSo
from dsps import DanhSachPs

'''a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3, 5)
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")'''

ps1 = PhanSo(3, 5)
ds = DanhSachPs()
ds.them(ps1)
ds.them(PhanSo(4, 6))
ds.docTuFile(r"C:\\Users\anhtt\Downloads\Python\2116985_PY_Lab02\dulieu.txt")
ds.xuat()
print(ds.demPsAm())
ds.layDsPsAm().xuat()
ds.layDsPsDuong().xuat()