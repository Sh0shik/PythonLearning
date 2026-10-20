ip = input()
parts = ip.split(".")
correct = len(parts) == 4
for p in parts:
    if not (p.isascii() and p.isdigit()) or int(p) > 255 or (len(p) > 1 and p[0] == "0"):
        correct = False
        break
print("YES" if correct else "NO")
