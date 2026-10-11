#ABC479-B
input()

s = input()

ans = 0
cnt = 0
for char in s:
    if char == 'R':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)