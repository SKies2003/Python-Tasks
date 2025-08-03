num = int(input("Enter a number: "))

def is_prime(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for i in range(2, num+1):
    if is_prime(i):
        while num%i == 0:
            print(i, end = " ")
            num //= i