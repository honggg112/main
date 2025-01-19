n = int(input())
xh = [list(map(int,input().split())) for _ in range(n)]
cut=2 ; rsp=0
if n<3: cut=n   # 一两个树而已
for i in range(1,n-1): # 除了第一你最后一个
    h = xh[i][1]
    if h < xh[i][0] - xh[i-1][0] - rsp: # 向左倒
        cut += 1 ; rsp = 0              # 右无位
    elif h < xh[i+1][0] - xh[i][0]:     # 向右倒
        cut += 1 ; rsp = h              # 右边占了'h'个位子
    else: rsp=0                         # 不砍树
print(cut)