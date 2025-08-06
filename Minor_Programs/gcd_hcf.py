a, b = map(int, input("Enter 2 numbers seperated by space: ").split())

# Euclidean Approach
def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(b-a, a)

print(gcd(a, b))

# Optimized Euclidean Approach

def opt_gcd(a: int, b: int) -> int:
    if a == 0:
        return a
    if b == 0:
        return b
    
    if a == b:
        return a
    elif a>b:
        if a%b == 0:
            return b
        return opt_gcd(a-b, b)
    else:
        if b%a == 0:
            return a
        return opt_gcd(b-a, a)

print(opt_gcd(a, b))

# Best approach

def best_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return best_gcd(b, a%b) # lowest time complexity = O(log(min(a, b)))