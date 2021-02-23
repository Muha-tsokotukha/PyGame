s = input()
x = 0
for x in range(0, len(s)):
    if s[x]==".":
       print('[',s[x],']',sep="",end="" )
    else: print(s[x],end="")
    x += 1 