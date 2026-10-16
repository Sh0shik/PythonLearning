
words = []
while True:
    value = input()
    if value == "":
        break
    if value not in words:
        words.append(value)

print(*words, sep='\n')
