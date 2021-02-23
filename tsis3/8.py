s = sorted(set(input().split()).intersection(set(input().split())))
for x in s:
    print(x, end = " ")