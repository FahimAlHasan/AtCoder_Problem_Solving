#ABC479-A
input()

a = list(map(int, input().split()))

print(sum(x for i, x in enumerate(a) if i % 2 == 0))