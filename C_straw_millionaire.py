#ABC454-C 

#verdict: AC

#I was sure that my logic was all correct. So I looked up to the editorial.
#I found that they used bfs algorithm whereas I used dfs algorithm. So no way to get RE.
#Then I asked for help from Gemini. 
#I came to konw that python has default recursion depth limit. We can modify that using sys.recursionlmiit


import sys
sys.setrecursionlimit(300_005)

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