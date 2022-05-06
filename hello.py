fp = open('D:/study/python/tcp school/ch1/PYTHON/temp.txt', 'r', encoding='utf-8')

file_data = fp.read()
print(file_data)

fp.close()

with open('D:/study/python/tcp school/ch1/PYTHON/temp.txt', 'r', encoding='utf-8') as fp2:
    file_data2 = fp2.read()
    print(file_data2)
    