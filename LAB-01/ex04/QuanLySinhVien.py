from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    # Thêm sinh viên
    def them_sinh_vien(self, ten, gioi_tinh, chuyen_nganh, dtb):
        sv = SinhVien(ten, gioi_tinh, chuyen_nganh, dtb)
        self.danh_sach.append(sv)
        print(f"Đã thêm sinh viên: {sv}")

    # Cập nhật thông tin sinh viên theo ID
    def cap_nhat_sinh_vien(self, id, ten=None, gioi_tinh=None, chuyen_nganh=None, dtb=None):
        sv = self.tim_sinh_vien_theo_id(id)
        if sv:
            if ten:
                sv.ten = ten
            if gioi_tinh:
                sv.gioi_tinh = gioi_tinh
            if chuyen_nganh:
                sv.chuyen_nganh = chuyen_nganh
            if dtb is not None:
                sv.dtb = dtb
                sv.hoc_luc = sv.tinh_hoc_luc(dtb)
            print(f"Thông tin sinh viên đã được cập nhật: {sv}")
        else:
            print("Sinh viên không tìm thấy.")

    # Xóa sinh viên theo ID
    def xoa_sinh_vien(self, id):
        sv = self.tim_sinh_vien_theo_id(id)
        if sv:
            self.danh_sach.remove(sv)
            print(f"Đã xóa sinh viên: {sv}")
        else:
            print("Sinh viên không tìm thấy.")

    # Tìm kiếm sinh viên theo tên
    def tim_sinh_vien_theo_ten(self, ten):
        ket_qua = [sv for sv in self.danh_sach if ten.lower() in sv.ten.lower()]
        return ket_qua

    # Tìm kiếm sinh viên theo ID
    def tim_sinh_vien_theo_id(self, id):
        for sv in self.danh_sach:
            if sv.id == id:
                return sv
        return None

    # Sắp xếp danh sách sinh viên theo DTB
    def sap_xep_theo_dtb(self):
        self.danh_sach.sort(key=lambda sv: sv.dtb, reverse=True)

    # Hiển thị danh sách sinh viên
    def hien_thi_danh_sach(self):
        if not self.danh_sach:
            print("Danh sách sinh viên trống.")
        else:
            for sv in self.danh_sach:
                print(sv)
