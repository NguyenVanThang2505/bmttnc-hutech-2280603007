print("Nhập các dòng văn bản (Nhập 'xong' để kết thúc): ")
lines =[]
while True:
    line = input()
    if line.lower() == 'xong':
        break
    lines.append(line)
    print("\n Các dòng đã nhập sau khi chuyển thành chữ in hoa:")
    for line in lines:
        print(line.upper())