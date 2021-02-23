'''count=int(input().strip())
for _ in range(count):
    ans=False
    try:
        string=input().strip()
        number=float(string)
        ans=True
        number=int(string)
        ans=False
    except:
        pass
    print(ans)
'''
import re
arr = list()
for _ in range(int(input())):
    arr.append((bool(re.match("^[\+-]?\d*\.\d+$", input()))))
for x in arr:
    print(x)