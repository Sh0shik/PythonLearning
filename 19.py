strList = input().split()
maxSym = 0
maxStr = ""
for i in strList:
    if len(i) > maxSym:
        maxSym = len(i)
        maxStr = i
print(maxStr)
print(maxSym)