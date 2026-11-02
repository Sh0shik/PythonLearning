n = int(input())
possible = set(range(1, n + 1))

while True:
    line = input().strip()
    if line == "HELP":
        break
    numbers = set(map(int, line.split()))
    answer = input().strip()
    if answer == "YES":
        possible &= numbers
    else:
        possible -= numbers

print(*sorted(possible))
