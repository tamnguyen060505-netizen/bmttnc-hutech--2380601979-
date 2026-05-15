def dao_nguoc_list(lst):
    return lst[::-1]

#Nhap danh sach tu nguoi dung va xu ly chuoi
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

#Su dung ham va in ket qua
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc:", list_dao_nguoc)