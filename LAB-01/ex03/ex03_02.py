def daoNguocDanhSach(lst):
    return lst[::-1]

input_str = input("Nhập các phần tử trong danh sách (cách nhau bởi dấu phẩy): ")
danhSach = [int(x) for x in input_str.split(',')]

danhSachDaoNguoc = daoNguocDanhSach(danhSach)
print(f"Danh sách sau khi đảo ngược là: {danhSachDaoNguoc}")
