#ABC460-C

n, m = map(int, input().split())

a = sorted(map(int, input().split()))

b = sorted(map(int, input().split()))

j, ans = 0, 0
for i in range(n):
    if j < m and b[j] <= a[i] * 2:
        ans += 1
        j += 1

print(ans)