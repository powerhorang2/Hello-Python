result = 0
line1 = '5 8 3'  # 입력 값을 받아야하는데 String 변수로 임의의 값을 지정함
line2 = '2 4 5 4 6'  # 입력 값을 받아야하는데 String 변수로 임의의 값을 지정함

array1 = line1.split(' ')
array2 = line2.split(' ')

n = int(array1[0])
m = int(array1[1])
k = int(array1[2])

array2.sort()

array = []
for i in array2:
    array.append(int(i))

# map 과 int 함수를 사용해서 데이터를 추출하면 되는데 직접 타입변환함

i = 0
for _ in range(m):
    if i < k:
        result += array[n - 1]
        i += 1
    else:
        result += array[n - 2]
        i = 0
# m 이라는 반복 기준이 있는데 i 변수를 생성해서 사용함
# while 문을 사용해서 해결 가능함


print("결과: ", result)
