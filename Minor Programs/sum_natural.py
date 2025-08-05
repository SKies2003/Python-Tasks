n = int(input("Enter a number: "))

# Beginner's/Iterative approach
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Recursive Approach
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)

print(sum_natural(n))

# Mathematical approach
print(((n+1)*n)//2)