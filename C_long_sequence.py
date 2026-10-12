#ABC457-C

n, k = map(int, input().split())

a = [list(map(int, input().split()))[1:] for _ in range(n)]

final_size = 0
for i, c in enumerate(map(int, input().split())):
    ith_list_size = len(a[i])

    if final_size + c * ith_list_size >= k:
        print(a[i][(k - final_size - 1) % ith_list_size])
        break
    
    final_size += c * ith_list_size