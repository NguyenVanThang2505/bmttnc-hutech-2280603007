def taoTupleTuDanhSach(lst):
    return tuple(lst)  

input_str = input("Nhập các phần tử trong danh sách (cách nhau bởi dấu phẩy): ")
danhSach = [x.strip() for x in input_str.split(',')]

tupleTuDanhSach = taoTupleTuDanhSach(danhSach)
print(f"Tuple tạo ra từ danh sách là: {tupleTuDanhSach}")
