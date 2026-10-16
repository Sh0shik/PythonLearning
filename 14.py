N, K = map(int, input().split())
lstN = list(map(int, input().split())).sort()
lstK = list(map(int, input().split()))
lstN = lstN[:N]
lstK = lstK[:K]
for i in lstK:
    left = 0
    right = N - 1
    while left < right:
        mid = (left + right) // 2
        if lstN[mid] < i:
            left = mid + 1
        else:
            right = mid
    if lstN[left] == i:
        print("YES")
    else:
        print("NO")
