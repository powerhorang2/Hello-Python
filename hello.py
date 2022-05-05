PATH = "D:/study/python/tcp school/ch1/PYTHON/temp.txt"
f = open(PATH, 'a', encoding='utf-8')

for i in range(6, 11):
    line = "%d번째 줄.\n" %i
    f.write(line)

f.close()