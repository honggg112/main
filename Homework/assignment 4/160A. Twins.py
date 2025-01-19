n= int(input())
a= list(map(int,input().split()))
a.sort(reverse= True)
total= sum(a)
my_coin = 0
num_division = 0
for i in a:
    my_coin += i
    num_division += 1
    if my_coin > total/2 :
        break

print(num_division)