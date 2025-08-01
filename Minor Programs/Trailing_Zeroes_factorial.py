n = int(input("Enter a num: "))

if n < -1:
    print(-1)

count = 0
i = 5
while n//i >= 1:
    count += n//i
    i *= 5
print(count)