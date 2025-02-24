from QuanLySinhVien import QuanLySinhVien

def menu():
    qlsv = QuanLySinhVien()
    while True:
        print("\n----- MENU -----")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp sinh viên theo DTB")
        print("6. Hiển thị danh sách sinh viên")
        print("7. Thoát")
        
        lua_chon = input("Chọn chức năng (1-7): ")

        if lua_chon == '1':
            ten = input("Nhập tên sinh viên: ")
            gioi_tinh = input("Nhập giới tính sinh viên: ")
            chuyen_nganh = input("Nhập chuyên ngành: ")
            dtb = float(input("Nhập điểm trung bình: "))
            qlsv.them_sinh_vien(ten, gioi_tinh, chuyen_nganh, dtb)
        
        elif lua_chon == '2':
            id = int(input("Nhập ID sinh viên cần cập nhật: "))
            ten = input("Nhập tên mới (bỏ qua nếu không thay đổi): ")
            gioi_tinh = input("Nhập giới tính mới (bỏ qua nếu không thay đổi): ")
            chuyen_nganh = input("Nhập chuyên ngành mới (bỏ qua nếu không thay đổi): ")
            dtb = input("Nhập điểm trung bình mới (bỏ qua nếu không thay đổi): ")
            dtb = float(dtb) if dtb else None
            qlsv.cap_nhat_sinh_vien(id, ten, gioi_tinh, chuyen_nganh, dtb)
        
        elif lua_chon == '3':
            id = int(input("Nhập ID sinh viên cần xóa: "))
            qlsv.xoa_sinh_vien(id)
        
        elif lua_chon == '4':
            ten = input("Nhập tên sinh viên cần tìm: ")
            ket_qua = qlsv.tim_sinh_vien_theo_ten(ten)
            if ket_qua:
                for sv in ket_qua:
                    print(sv)
            else:
                print("Không tìm thấy sinh viên với tên đó.")
        
        elif lua_chon == '5':
            qlsv.sap_xep_theo_dtb()
            print("Danh sách sinh viên đã được sắp xếp theo DTB.")
        
        elif lua_chon == '6':
            qlsv.hien_thi_danh_sach()
        
        elif lua_chon == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
