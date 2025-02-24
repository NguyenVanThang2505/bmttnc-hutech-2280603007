def tongSoChan(lst):
    tong = 0
    for so in lst:
        if so % 2 == 0:  
            tong += so  
    return tong

input_str = input("Nhập các số (cách nhau bởi dấu phẩy): ")
danhSach = [int(x) for x in input_str.split(',')]

ketQua = tongSoChan(danhSach)
print(f"Tổng tất cả số chẵn trong danh sách là: {ketQua}")