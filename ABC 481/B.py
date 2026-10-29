#ABC481-B
#verdict: AC

_, k = map(int, input().split())

nums = list(map(int, input().split()))

print(sum(1 if a < k <= b or a > k >= b else 0 for a, b in zip(nums, nums[1:])) + int(nums[0] == k))