n, m = map(int, input().split())
x, y, direction = map(int, input().split())
# 방문 기록 저장용
history = [[0] * m for _ in range(n)]

history[x][y] = 1  # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    turn_time += 1
    if array[nx][ny] != 1 and history[nx][ny] != 1:
        turn_time = 0
        x, y = nx, ny
        history[x][y] = 1
        count += 1
        continue
    if turn_time == 5:
        turn_time = 0
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 1:
            break
        x, y = nx, ny

print("x, y: ", x, y)
print("count: ", count)
