result = 0
line1 = '5 8 3'
line2 = '2 4 5 4 6'

array1 = line1.split(' ')
array2 = line2.split(' ')

n = int(array1[0])
m = int(array1[1])
k = int(array1[2])

array2.sort()

array = []
for i in array2:
    array.append(int(i))

i = 0
for _ in range(m):
    if i < k:
        result += array[n - 1]
        i += 1
    else:
        result += array[n - 2]
        i = 0

print("결과: ", result)
