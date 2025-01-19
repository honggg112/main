L,M = map(int,input().split())
trees = [1]*(L+1)

for i in range(M):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        trees [j]  =0

print(trees.count(1))
