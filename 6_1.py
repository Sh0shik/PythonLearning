
# File = open("6_1.txt")
import sys
File = sys.stdin
parties = {}
while True:
    line = File.readline()
    if line == "VOTES:\n":
        break
    if line == "PARTIES:\n":
        continue
    parties.setdefault(line.strip(), 0)

while True:
    line = File.readline()
    if line == "":
        break
    parties[line.strip()] = parties.get(line.strip()) + 1

File.close()

result = sorted(parties.items(), key=lambda x: (-x[1], x[0]))
for party in result:
    print(party[0])