# Улитка
import math
h = int(input())
a = int(input())
b = int(input())
distant = max(0, (h - b - 1) // (a - b)) + 1
print(distant)