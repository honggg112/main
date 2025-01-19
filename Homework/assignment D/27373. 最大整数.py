limit = int(input())
n = int(input())
lst = list(map(str, input().split()))

def sorting(a, b):
    if int(a + b) > int(b + a):
        return True
    else:
        return False

for i in range(n):
    for j in range(i, n):
        if not sorting(lst[i], lst[j]):
            lst[i], lst[j] = lst[j], lst[i]

dp = [0] * (limit + 1)               # dp[i]表示i位数时最大值
temp = [0] * (limit + 1)
for j in lst:
    for i in range(len(j), limit + 1):
        dp[i] = max(dp[i], int(str(temp[i - len(j)]) + j))
    temp[:] = dp
print(dp[limit])