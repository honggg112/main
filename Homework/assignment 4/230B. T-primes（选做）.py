input()
num = [int(x)** (0.5) for x in input().split()]
mx = int(max(num))
prime = set() ; isprime = [1]*(mx-1)

for i in range(2,mx+1):
    if isprime[i-2]:
        prime.add(i)
        for j in range(i**2,mx+1,i): isprime[j-2]=0
for x in num: print(['NO','YES'][x in prime])