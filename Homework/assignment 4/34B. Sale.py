n,m = map(int,input().split())
a= list(map(int,input().split()))
a.sort()
profit = 0
for i in range(m):
    if a[i]< 0:
        profit += a[i]
    else:
        break

print(abs(profit))