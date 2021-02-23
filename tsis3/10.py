syns = { '#' : '$' }
n = int(input())
while n > 0:
    s = input().split()
    syns[s[0]] = s[1]
    n -= 1
word = str(input())
for x in syns:
    if x == word:
        print( syns[x] )
        break
    elif  syns[x] == word:
        print( x )
        break