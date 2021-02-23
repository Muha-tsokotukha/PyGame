coun = dict()
n = int(input())
while n > 0:
    n -= 1
    x = input().split()
    for y in x :
        t = True
        for q in coun:
            if q == y :
                coun[q] += 1
                t = False
                break
        if t:
            coun[y] = 1
for w in coun:
    print( coun[w] ,end=" " )
