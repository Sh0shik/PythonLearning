text = input()
result = ""
space_needed = False
for ch in text:
    if ch == " ":
        space_needed = True
    elif ch == "," or ch == ".":
        result += ch
        space_needed = True
    else:
        if space_needed and result != "":
            result += " "
        result += ch
        space_needed = False
print(result)
