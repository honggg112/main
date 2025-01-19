p = int(input())
weapon = sorted(map(int, input().split()))

if p < weapon[0]:
    ans = 0
else:
    me = enemy = 0
    while weapon:
        make = weapon[0]
        sell = weapon[-1]
        if p >= make:
            p -= make
            me += 1
            del weapon[0]
        elif len(weapon) > 2 and sell + p >= make:
            p += sell
            enemy += 1
            del weapon[-1]
        else: break
    ans = me - enemy
print(ans)

"""
p = int(input())
w = list(map(int, input().split()))
w.sort()

# 将列表转换为 deque
w = deque(w)

a = 0  # 记录购买的物品数量
b = 0  # 记录退回的物品数量

while len(w) > 0:
    while p > 0 and len(w) > 0:
        if p >= w[0]:
            p -= w.popleft()  # 从左侧移除并更新剩余金额
            a += 1
        else:
            break

    if len(w) <= 1:  # 如果只剩下一个或没有物品，则退出循环
        break

    if a > b:
        p += w.pop()  # 从右侧移除并增加剩余金额
        b += 1
    else:
        break
print(a - b)
"""