pos = input()

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = row.index(pos[0]) + 1
y = int(pos[1])

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    result += 1

print(result)
