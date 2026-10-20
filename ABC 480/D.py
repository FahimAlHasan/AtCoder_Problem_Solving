#ABC480-C
#verdict: AC
#seems like I make the calculations overcomplicated...also the variable names seem verbose

import bisect

n, q = map(int, input().split())

a = list(map(int, input().split()))

packets_length_sum = [0]
for i in range(1, n + 1):
    packets_length_sum.append(packets_length_sum[-1] + i)

cumulative_sum = 0
each_packets_own_sum = [0]
for x in a:
    cumulative_sum += x
    each_packets_own_sum.append(cumulative_sum)

packets_cumulative_sum = [0]
for x in each_packets_own_sum[1:]:
    packets_cumulative_sum.append(packets_cumulative_sum[-1] + x)
     
for _ in range(q):
    l, r = map(int, input().split())

    i = bisect.bisect_left(packets_length_sum, l)
    j = bisect.bisect_left(packets_length_sum, r)

    answer = packets_cumulative_sum[j] - packets_cumulative_sum[i - 1]

    left_discard = l - ((i * (i - 1)) // 2 + 1)
    answer -= each_packets_own_sum[left_discard]
    # print(left_discard)

    right_discard = r - ((j * (j - 1)) // 2)
    answer -= each_packets_own_sum[j] - each_packets_own_sum[right_discard]

    print(answer)

    