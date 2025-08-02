# Write a program where if no. of even digits are more than odd digits display True else False

n = int(input("Enter a number: "))

even, odd = 0, 0
while n>0:
    x = n%10
    if x%2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

if even > odd:
    print(True)
else:
    print(False)