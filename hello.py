# 그래프는 딕셔너리로 감싸고 그 안의 벨류 값을 리스트로 구현
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# 재귀 호출로 구현
def recursive_dfs(v, visited=[]):
    visited.append(v)  # 시작 정점 방문
    for w in graph[v]:
        if w not in visited:  # 방문 하지 않았으면
            visited = recursive_dfs(w, visited)
    return visited


# 스택으로 구현
def iterative_dfs(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


print("recursive_dfs: ", recursive_dfs(1))
print("iterative_dfs: ", iterative_dfs(1))
