import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

root = Tk()

root.title("Đăng ký học phần")
root.geometry('640x360')
root.configure(background = 'light green')

lbl = Label(root, text = "THÔNG TIN ĐĂNG KÝ HỌC PHẦN", bg = 'light green', fg = "red", height = 2)
lbl.config(font = ("Helvaetica bold", 16))
lbl.grid(column = 1, row = 0)

lb2 = Label(root, text = "Mã số sinh viên", bg = 'light green', padx = 3, pady = 3)
lb2.config(font = ("Helvaetica bold", 10))
lb2.grid(column = 0, row = 1, sticky = W)
txtMaSo = Entry(root, width = 50)
txtMaSo.grid(column = 1, row = 1)

lb3 = Label(root, text = "Họ tên", bg = 'light green', padx = 3, pady = 3)
lb3.config(font = ("Helvaetica bold", 10))
lb3.grid(column = 0, row = 2, sticky = W)
txtHoTen = Entry(root, width = 50)
txtHoTen.grid(column = 1, row = 2)

lb4 = Label(root, text = "Ngày sinh", bg = 'light green', padx = 3, pady = 3)
lb4.config(font = ("Helvaetica bold", 10))
lb4.grid(column = 0, row = 3, sticky = W)
txtNgaySinh = Entry(root, width = 50)
txtNgaySinh.grid(column = 1, row = 3)

lb5 = Label(root, text = "Email", bg = 'light green', padx = 3, pady = 3)
lb5.config(font = ("Helvaetica bold", 10))
lb5.grid(column = 0, row = 4, sticky = W)
txtEmail = Entry(root, width = 50)
txtEmail.grid(column = 1, row = 4)

lb6 = Label(root, text = "Số điện hoại", bg = 'light green', padx = 3, pady = 3)
lb6.config(font = ("Helvaetica bold", 10))
lb6.grid(column = 0, row = 5, sticky = W)
txtSdt = Entry(root, width = 50)
txtSdt.grid(column = 1, row = 5)

lb7 = Label(root, text = "Học kỳ", bg = 'light green', padx = 3, pady = 3)
lb7.config(font = ("Helvaetica bold", 10))
lb7.grid(column = 0, row = 6, sticky = W)
txtHocKy = Entry(root, width = 50)
txtHocKy.grid(column = 1, row = 6)

lb8 = Label(root, text = "Năm học", bg = 'light green', padx = 3, pady = 3)
lb8.config(font = ("Helvaetica bold", 10))
lb8.grid(column = 0, row = 7, sticky = W)
cbbNamHoc = ttk.Combobox(root, width = 47)
cbbNamHoc['values'] = ('2022 - 2023','2023 - 2024','2024 - 2025')
cbbNamHoc['state'] = 'readonly'
cbbNamHoc.grid(column = 1, row = 7)

lb9 = Label(root, text = "Chọn môn học", bg = 'light green', padx = 3, pady = 3)
lb9.config(font = ("Helvaetica bold", 10))
lb9.grid(column = 0, row = 8, sticky = W)

Check1 = IntVar()
cb1 = Checkbutton(root, variable = Check1, text = "Lập trình Python", bg = 'light green')
cb1.grid(column = 1, row = 8, sticky = W)

Check2 = IntVar()
cb2 = Checkbutton(root, variable = Check2, text = "Lập trình Java                    ", bg = 'light green')
cb2.grid(column = 1, row = 8, sticky = E)

Check3 = IntVar()
cb3 = Checkbutton(root, variable = Check3, text = "Công nghệ phần mềm", bg = 'light green')
cb3.grid(column = 1, row = 9, sticky = W)

Check4 = IntVar()
cb4 = Checkbutton(root, variable = Check4, text = "Phát triển ứng dụng web", bg = 'light green')
cb4.grid(column = 1, row = 9, sticky = E)

def clicked():
    if (txtMaSo.get() == "" or txtMaSo.get().isdigit() == False or len(txtMaSo.get()) < 7 or len(txtMaSo.get()) > 7):
        lbl.configure(text = "Mã số sinh viên không hợp lệ!")
        lbl.grid(column = 2, row = 1, sticky = W)
        return
    else:
        lbl.configure(text = "")
    
    if txtHoTen.get() == "":
        lbl.configure(text = "Chưa nhập tên!")
        lbl.grid(column = 2, row = 2, sticky = W)
        return
    else:
        lbl.configure(text = "")
    
    if txtNgaySinh.get() == "" or re.search(r'^([0-9]{1,2}+)/([0-9]{1,2}+)/([0-9]{4})$', txtNgaySinh.get()) == None:
        lbl.configure(text = "Thông tin không hợp lệ!")
        lbl.grid(column = 2, row = 3, sticky = W)
        return
    else:
        s = txtNgaySinh.get().split("/")
        if (int(s[2]) < 1900 or int(s[2]) > 2023):
            lbl.configure(text = "Năm sinh không hợp lệ!")
            lbl.grid(column = 2, row = 3, sticky = W)
            return
        else:
            if (int(s[1]) < 1 or int(s[1]) > 12):
                lbl.configure(text = "Tháng sinh không hợp lệ!")
                lbl.grid(column = 2, row = 3, sticky = W)
                return
            else:
                if (int(s[0]) < 0 or int(s[0]) > 31):
                    lbl.configure(text = "Ngày sinh không hợp lệ!")
                    lbl.grid(column = 2, row = 3, sticky = W)
                    return
        lbl.configure(text = "")
    
    if txtEmail.get() == "" or re.search(r'^([a-z0-9_-]+)@([\da-z\.-]+)\.([a-z]{2,6})$', txtEmail.get()) == None:
        lbl.configure(text = "Email không hợp lệ!")
        lbl.grid(column = 2, row = 4, sticky = W)
        return
    else:
        lbl.configure(text = "")

    if txtSdt.get() == "" or txtSdt.get().isdigit() == False or len(txtSdt.get()) < 10 or len(txtSdt.get()) > 10:
        lbl.configure(text = "Số điện thoại không hợp lệ!")
        lbl.grid(column = 2, row = 5, sticky = W)
        return
    else:
        lbl.configure(text = "")
    
    if txtHocKy.get() == "" or txtHocKy.get().isdigit() == False or int(txtHocKy.get()) < 1 or int(txtHocKy.get()) > 3:
        lbl.configure(text = "Học kỳ không hợp lệ! (1 - 2 - 3)")
        lbl.grid(column = 2, row = 6, sticky = W)
        return
    else:
        lbl.configure(text = "")
    
    if (Check1.get() == 0 and Check2.get() == 0 and Check3.get() == 0 and Check4.get() == 0):
        lbl.configure(text = "Chưa chọn môn học!")
        lbl.grid(column = 2, row = 8, sticky = W)
        return
    else:
        lbl.configure(text = "")
    saveToExcel()
    
def saveToExcel():
    pass

lbl = Label(root, text = "", bg = 'light green', fg = 'red', padx = 3, pady = 3)
lbl.config(font = ("Helvaetica bold", 10))

btnDk = Button(root, text = "Đăng ký", bg = "#00ff00", command = clicked)
btnDk.grid(column = 1, row = 10, sticky = W)

btnThoat = Button(root, text = "Thoát", bg = "#00ff00", command = root.quit)
btnThoat.grid(column = 1, row = 10, sticky = E)

root.mainloop()