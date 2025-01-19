num = 0

while True:
    p, e, i, d, = map(int, input().split())
    if [p, e, i, d] == [-1, -1, -1, -1]:
        break
    num += 1

    D = d+1
    while (D-p)%23 != 0 or (D-e)%28 != 0 or (D-i)%33 != 0:
        D += 1

    D -=d
    print(f'Case {num}: the next triple peak occurs in {D} days.')
