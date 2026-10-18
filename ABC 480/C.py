#ABC-480C

n, k, t = map(int, input().split())

a = list(map(int, input().split()))
a.append(t)
a = sorted(a)

taps, last = 1, k
if a[0] == 0:
    taps = 0
    a = a[1:]
    
for num in a:
    if num > t:
        break
    if num > last:
        d = (num - last + k - 1) // k
        taps += d
    last = num + k

print(taps)
