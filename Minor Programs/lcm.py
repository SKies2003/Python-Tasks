a, b = map(int, input("Enter two numbers seperated by space: ").split())

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a%b)
print((a*b)// gcd(a, b))