intput_str = input("Nhập x và y: ")
dimensions = [int (x) for x in intput_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilsit = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilsit[row][col] = row*col
print (multilsit)