n = int(input())
a = list(map(int, input().split()))

crime = 0
officer = 0
for i in a:
    if i == -1:
        if officer > 0:
            officer -= 1
        else:
            crime += 1
    elif i>0:
        officer += i

print(crime)