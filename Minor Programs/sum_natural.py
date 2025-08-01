n = int(input("Enter a number: "))

# Beginner's approach
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# Mathematical approach
print(((n+1)*n)//2)