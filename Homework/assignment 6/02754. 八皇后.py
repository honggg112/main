list1 = []

def queen(s):
    if len(s)== 8:
        list1.append(s)
        return
    for i in range(1,9):
        if all(str(i)!= s[j] and abs(len(s)-j)!= abs(i - int(s[j]))for j in range(len(s))):
            queen(s + str(i))

queen("")
samples = int(input())
for k in range(samples):
    print(list1[int(input())-1])