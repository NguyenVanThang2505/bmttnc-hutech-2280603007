def daoNguocChuoi(chuoi):
    return chuoi[::-1]

chuoi = input("Nhập chuỗi để đảo ngược: ")
chuoiDaoNguoc = daoNguocChuoi(chuoi)
print(f"Chuỗi đảo ngược là: {chuoiDaoNguoc}")