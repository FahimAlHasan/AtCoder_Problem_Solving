#ABC482 - C
#verdict: AC

from bisect import bisect_left, bisect_right

h, w, n, q = map(int, input().split())

row, col = [], []
for _ in range(n):
    r, c = map(int, input().split())
    row.append(r)
    col.append(c)

row.sort()
col.sort()

for _ in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        print(bisect_right(row, r) - bisect_left(row, l))
    else:
        print(bisect_right(col, r) - bisect_left(col, l))