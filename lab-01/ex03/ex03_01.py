def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

#Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

#Su dung ham va in ket qua
tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong list la: ", tong_chan)