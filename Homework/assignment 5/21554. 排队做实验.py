# odd code remastered
n = int(input())
queue = [*map(int, input().split())]
q_sort = sorted(queue)
q_indx = []
j = time = 0
for k in range(n-1, -1, -1):
    time += q_sort[j]*k
    i = queue.index(q_sort[j])
    q_indx.append(i+1)
    queue[i] = 0
    j += 1
print(*q_indx)
print('%.2f'%(time/n))