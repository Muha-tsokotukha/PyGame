arr = list(map(int, input().split()))
sq = list()
for x in arr:
    sq.append(x**2)
print(*sq)