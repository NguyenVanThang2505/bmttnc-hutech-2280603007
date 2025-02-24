def xoaPhanTuTheoKey(d, key):
    if key in d:
        del d[key]  
        print(f"Đã xóa phần tử với key: {key}")
    else:
        print(f"Key '{key}' không tồn tại trong dictionary.")

dictionary = {
    "apple": 5,
    "banana": 3,
    "orange": 7
}

keyCanXoa = input("Nhập key của phần tử cần xóa: ")

xoaPhanTuTheoKey(dictionary, keyCanXoa)

print("Dictionary sau khi xóa phần tử:")
print(dictionary)
