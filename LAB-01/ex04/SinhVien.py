class SinhVien:
    def __init__(self, ten, gioi_tinh, chuyen_nganh, dtb):
        self.id = SinhVien.tang_id()  
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.dtb = dtb
        self.hoc_luc = self.tinh_hoc_luc(dtb)

    # Tính học lực dựa trên điểm trung bình
    def tinh_hoc_luc(self, dtb):
        if dtb >= 8:
            return "Giỏi"
        elif 6.5 <= dtb < 8:
            return "Khá"
        elif 5 <= dtb < 6.5:
            return "Trung bình"
        else:
            return "Yếu"
    
    # Tạo ID tự động
    _id = 0
    @classmethod
    def tang_id(cls):
        cls._id += 1
        return cls._id
    
    # Hàm để hiển thị thông tin sinh viên
    def __str__(self):
        return f"ID: {self.id}, Tên: {self.ten}, Giới tính: {self.gioi_tinh}, Chuyên ngành: {self.chuyen_nganh}, DTB: {self.dtb}, Học lực: {self.hoc_luc}"
