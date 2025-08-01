n = int(input("Enter a num: "))

reverse = 0
temp = n # To preserve n for later comparison

while temp>0:
    last_digit = temp%10
    reverse = 10*reverse + last_digit
    temp //= 10

if reverse == n:
    print(True)
else:
    print(False)

# Smaller approach good for small number but bad for larger one, and more space consuming than previous one.
n_str = str(n)
if n_str == n_str[::-1]:
    print(True)
else:
    print(False)