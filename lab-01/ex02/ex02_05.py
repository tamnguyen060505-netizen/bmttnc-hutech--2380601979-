So_gio_lam = float(input("Nhap so gio lam moi tuan: "))
Luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
Gio_tieu_chuan = 44 #So gio lam moi tuan
Gio_vuot_chuan = max(0, So_gio_lam - Gio_tieu_chuan) #So gio lam vuot moi tuan
Thuc_linh = Gio_tieu_chuan * Luong_gio + Gio_vuot_chuan * Luong_gio * 1.5 #Tinh tong thu nhap
print(f"So tien thuc linh cua nhan vien: {Thuc_linh}")