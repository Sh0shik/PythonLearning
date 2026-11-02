n = int(input())

# сколько выборщиков у каждого штата
electors = {}
for i in range(n):
    state, count = input().split()
    electors[state] = int(count)

# votes[штат][кандидат] = сколько голосов
votes = {}
# result[кандидат] = сколько выборщиков (сначала 0 у всех кандидатов)
result = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    if line.strip() == "":
        break
    state, cand = line.split()

    votes.setdefault(state, {})
    votes[state][cand] = votes[state].get(cand, 0) + 1
    result.setdefault(cand, 0)

# сколько выборщиков набрал каждый кандидат
for state in votes:
    best_cand = ""
    best_votes = 0
    for cand in votes[state]:
        v = votes[state][cand]
        # больше голосов, или поровну, но имя раньше по алфавиту
        if v > best_votes or (v == best_votes and cand < best_cand):
            best_votes = v
            best_cand = cand

    result[best_cand] = result.get(best_cand, 0) + electors[state]

# сортировка: сначала у кого больше выборщиков, потом по имени
for cand, count in sorted(result.items(), key=lambda x: (-x[1], x[0])):
    print(cand, count)


# # сортировка: сначала у кого больше выборщиков, потом по имени
# # каждый раз находим лучшего, выводим и убираем из словаря
# while len(result) > 0:
#     best_cand = ""
#     best_count = -1
#     for cand in result:
#         count = result[cand]
#         # больше выборщиков, или поровну, но имя раньше по алфавиту
#         if count > best_count or (count == best_count and cand < best_cand):
#             best_count = count
#             best_cand = cand

#     print(best_cand, best_count)
#     del result[best_cand]
