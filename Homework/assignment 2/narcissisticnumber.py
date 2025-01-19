a, b = map(int, input().split())
result =[]

for n in range(a, b + 1):
    hundreds = n // 100
    tens = (n % 100) // 10
    units = n % 10
    if hundreds ** 3 + tens ** 3 + units ** 3 == n:
        result.append(n)
if result:
    print(*result)
else:
    print("NO")

"""
a,b = map(int,input().split())
result= []

for i in range(a,b+1):
    x= i //100
    y= (i-100*x)//10
    z= (i-100*x-10*y)
    if x**3 + y**3 + z**3 == i:
        result.append(i)
if not result:
    print("NO")
else:
    print(*result)
"""