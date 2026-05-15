#Nhap so tu nguoi dung
So = int(input("Nhap mot so nguyen: "))
#Kiem tra xem so do co phai la so chan hay khong
if So % 2 == 0:
    print(So, "la so chan.")
else:
    print(So, "khong phai la so chan.")