# for i in range(len(a) // 2):
#     a[i], a[-1 - i] = a[-1 - i], a[i]
# # или a.reverse(), a[::-1]

lst = list(map(int, input().split()))
lst.reverse()
print(*lst)