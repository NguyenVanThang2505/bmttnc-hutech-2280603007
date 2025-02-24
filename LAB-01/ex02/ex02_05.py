workingTime = float(input("Nhập số giờ làm mỗi tuần: "))
salaryPerHour = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
standardTime = 44
overStandard = max(0, workingTime - standardTime)
salary = standardTime * salaryPerHour + overStandard * salaryPerHour * 1.5
print(f"Sô tiền thực lĩnh của bạn là: {salary}")