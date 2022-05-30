from collections import deque

n, m, start = map(int, input().split())

graph = []

for _ in m:
    graph.append(list(map(int, input().split())))

dfs_visited = [False] * n


def dfs(graph, start):
    dfs_visited[start - 1] = True