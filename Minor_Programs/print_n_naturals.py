n = int(input("Enter a number: "))

# Iteration
for i in range(1, n+1):
    print(i, end=" ")

# Recursion
def print_naturals(n):
    if n == 0:
        return
    print_naturals(n-1)
    print(n, end=" ")

print()
print_naturals(n)

### PRINT IN REVERSE

print()
# Iteration
for i in range(n, 0, -1):
    print(i, end=" ")

# Recursion
def reverse_naturals(n):
    if n == 0:
        return
    print(n, end=" ")
    reverse_naturals(n-1)

print()
reverse_naturals(n)