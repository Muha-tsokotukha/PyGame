a = set(input().split())
b = set(input().split())
cnt = 0
for x in a:
    for y in b:
        if x == y:
            cnt += 1
print(cnt)