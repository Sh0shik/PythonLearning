x, y = map(float, input().split())
a1 = '1' if y <= 1 else '0'
a2 = '1' if y <= -x else '0'
a3 = '1' if x**2 + y**2 <= 1 else '0'
a4 = '1' if (x - 1)**2 + y**2 <= 1 else '0'
print(a1 + a2 + a3 + a4)