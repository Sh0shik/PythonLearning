def typeTriangle(a, b, c):
    if pow(a, 2) == (pow(b, 2) + pow(c, 2)):
        print("right")
    elif pow(a, 2) < (pow(b, 2) + pow(c, 2)):
        print("acute")
    elif pow(a, 2) > (pow(b, 2) + pow(c, 2)):
        print("obtuse")
    else:
        print("impossible")

a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print("impossible")
elif a > b and a > c:
    typeTriangle(a, b, c)
elif b > a and b > c:
    typeTriangle(b, a, c)
else:
    typeTriangle(c, b, a)

