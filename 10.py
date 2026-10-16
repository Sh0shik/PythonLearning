
from random import randint

inputData = list(map(int, input().split()))
lst = [randint(inputData[0], inputData[1]) for x in range(inputData[2])]
print(*lst)

resultLst = []
for i in range(len(lst) // 2):
    sumEl = lst[i] + lst[-i-1]
    if sumEl % 2 == 0:
        resultLst.append([i, sumEl])

if len(resultLst) != 0:
    indMax = max(resultLst, key = lambda x: (x[1], x[0]))[0]
    print(indMax + 1, len(lst) - indMax, end = ' ')
else:
    print(0, 0, end = ' ')
