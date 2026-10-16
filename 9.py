import random

N = int(input())
lst = [x for x in range(1, N + 1) if x != 5]
for i in range(len(lst) - 1, 0, -1):
    j = random.randint(0, i)
    lst[i], lst[j] = lst[j], lst[i]
print(*([5] + lst))
