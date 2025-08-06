a = int(input("Enter first number for Arithmetic Progression: "))
d = int(input("Enter difference between elements: "))
n = int(input("Enter no. of elements in series: "))

# Iterative approach
sum = 0
i = 0
while i < n:
    sum += a+(i*d)
    i += 1
print(sum)

# Iterative approach is slower with a time complexity of O(n) and space complexity of O(1).

# Mathemtical approach
sum = (n/2)*(2*a + (n-1)*d)
print(int(sum))

# Mathematical approach is faster with time complexity of O(1) and space complexity of O(1).
