#ABC454-C 
#verdict: WA

n, m = map(int, input().split())

adjacent_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adjacent_list[u].append(v)

visited = [False for _ in range(n + 1)]
def dfs(u: int):
    visited[u] = True

    for v in adjacent_list[u]:
        if not visited[v]:
            dfs(v)

dfs(1)              

print(visited.count(True))