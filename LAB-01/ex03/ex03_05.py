def demSoLanXuatHien(lst):
    ketQua = {}
    for phanTu in lst:
        if phanTu in ketQua:
            ketQua[phanTu] += 1  
        else:
            ketQua[phanTu] = 1  
    return ketQua

input_str = input("Nhập các phần tử trong danh sách (cách nhau bởi dấu phẩy): ")
danhSach = [x.strip() for x in input_str.split(',')]  

ketQua = demSoLanXuatHien(danhSach)

print("Số lần xuất hiện của mỗi phần tử trong danh sách là:")
for phanTu, soLan in ketQua.items():
    print(f"{phanTu}: {soLan}")
