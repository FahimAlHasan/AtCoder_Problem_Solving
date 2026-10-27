#ABC481-D
#Verdict: AC

from collections import deque

n, m, s, t = map(int, input().split())

adj = [[] for _ in range(n + 1)]
min_adj = [None for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    if min_adj[u] == None:
        min_adj[u] = v
    else:
        min_adj[u] = min(min_adj[u], v)

dist = [None if i != s else 0 for i in range(n + 1)]
g = deque([s])
while g:
    u = g.popleft()
    for v in adj[u]:
        w = 0 if min_adj[u] == v else 1
        if dist[v] == None or dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            if w == 0:
                g.appendleft(v)
            else:
                g.append(v)

print(-1 if dist[t] == None else dist[t])