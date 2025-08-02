n = int(input("Enter a num: "))

# Iterative Approach
factorial = 1
for i in range(2, n+1):
    factorial *= i
print(factorial)

# Recursive Approach
def calc_factorial(n: int) -> int:
    if n < 2:
        return 1
    return n*calc_factorial(n-1) # It call cal_factorial again and again till n < 2.

print(calc_factorial(n))