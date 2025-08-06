# Write a program where we need to put all even digits together than odd digits together in reverse order.

n = int(input("Enter a number: "))

result = 0
odd = 0
while n>0:
    x = n%10
    if x%2 == 0:
        result = result*10 + x
    else:
        odd = odd*10 + x
    n //= 10

temp = odd
count = 0
while temp > 0:
    temp //= 10
    count += 1

result = result*(10**count)+odd
print(result)