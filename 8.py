import sys
sys.setrecursionlimit(1000000)

def ProstChislo(a, d = 2):
    if a < 2:
        return 0
    if d * d > a:
        return 1
    if a % d == 0:
        return 0
    return ProstChislo(a, d + 1)


a = int(input())
if ProstChislo(a):
    print("YES")
else:
    print("NO")