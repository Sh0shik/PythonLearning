def MaxMin():
    numbers = []
    while True:
        n = int(input())
        if n == 0:
            break
        numbers.append(n)
    print(min(numbers), end = ' ')
    print(max(numbers))

MaxMin()

