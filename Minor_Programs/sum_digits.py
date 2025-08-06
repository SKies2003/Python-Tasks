n = int(input("Enter a number: "))
x = n

# Using Iteration
sum = 0
while n > 0:
    sum += n%10
    n //= 10
print(sum)

# Using Recursion
def dSum(m):
    if m < 10:
        return m
    return dSum(m//10) + m%10

print(dSum(x))