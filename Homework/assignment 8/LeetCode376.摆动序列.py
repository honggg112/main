def sgn(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1


n = int(input())
nums = list(map(int, input().split()))
delta = [sgn(nums[i + 1] - nums[i]) for i in range(n - 1)]

result = 1
pre = 0
for i in range(n - 1):
    if delta[i] * pre < 0 or (pre == 0 and delta[i] != 0):
        result += 1
        pre = delta[i]

print(result)