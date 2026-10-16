# m = a[0]
# for x in a:
#     if x > m:
#         m = x

import copy
import random

def DeleteMaxMin(lst):
    maxEl = max(lst)
    minEl = min(lst)
    print(maxEl, minEl, end = '\n') 
    while maxEl in lst:
        lst.remove(maxEl)
    while minEl in lst:
        lst.remove(minEl)
    return lst

lst = [random.randint(1, 10)for x in range(int(input()))]
print(*lst)
copyLst = copy.copy(lst)
resultLst = DeleteMaxMin(copyLst)
if len(resultLst) != 0:
    print(*resultLst)

