def truyCapDauCuoi(tuple):
    if len(tuple) > 0:  
        dau = tuple[0] 
        cuoi = tuple[-1]  
        return dau, cuoi
    else:
        return None, None  

input_str = input("Nhập các phần tử trong tuple (cách nhau bởi dấu phẩy): ")
tupleNhap = tuple(x.strip() for x in input_str.split(','))  

dau, cuoi = truyCapDauCuoi(tupleNhap)

if dau is not None and cuoi is not None:
    print(f"Phần tử đầu tiên là: {dau}")
    print(f"Phần tử cuối cùng là: {cuoi}")
else:
    print("Tuple rỗng!")
