def kiemTraSoNguyenTo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
    return True

so = int(input("Nhập số để kiểm tra xem có phải là số nguyên tố không: "))
if kiemTraSoNguyenTo(so):
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
