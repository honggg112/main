line1 = input()
line2 = input()
if line1.lower() < line2.lower():
    print (-1)
elif line1.lower() > line2.lower():
    print (1)
else:
    print (0)