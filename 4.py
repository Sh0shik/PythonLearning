N = int(input())
if N <= 1:
    print('0')
while N > 0:
    if N % 2 == 0:
        print(pow(2, N), end=' ')
    N -= 1