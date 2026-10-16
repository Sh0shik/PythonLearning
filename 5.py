n = int(input())
count = 0
for a in range(n // 10 + 1):
    for b in range((n - 10*a) // 5 + 1):
        r = n - 10*a - 5*b
        count += r // 2 + 1
print(count)