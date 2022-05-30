from collections import deque

n, m = map(int, input().split())

miro = []

for i in range(n):
    miro.append(list(map(int, input())))

# 방향 (좌, 우, 상, 하)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    return miro[n - 1][m - 1]


print(bfs(0, 0))

for j in range(n):
    print(miro[j])
