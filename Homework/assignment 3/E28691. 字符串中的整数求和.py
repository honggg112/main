a,b =input().split()

# ord("0") = 48
x = ord(a[0])+ ord(b[0])-48-48
y = ord(a[1])+ ord(b[1])-48-48
print(x*10+y)