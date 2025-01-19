n = int(input())

while True:
    if n == 1:
        print("End")
        break
    elif n%2 != 0:
        print(n, end="")
        print("*3+1=", end="")
        n= n*3+1
        print(n)
    else:
        print(n,end="")
        print("/2=",end="")
        n=n//2
        print(n)

"""
def collatz_sequence(n):
    if n == 1:
        print("End")
        return

    while n != 1:
        if n % 2 == 1:
            next_n = 3 * n + 1
            print(f"{n}*3+1={next_n}")
        else:
            next_n = n // 2
            print(f"{n}/2={next_n}")
        n = next_n

    print("End")

# Sample input
n = int(input())

# Calculate and print the result
collatz_sequence(n)
"""