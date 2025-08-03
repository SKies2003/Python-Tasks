import math
num = int(input("Enter a number: "))

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

if check_prime(num):
    print("Prime")
else:
    print("Composite")