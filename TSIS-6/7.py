def UpLow(s):
    up = 0
    for x in s:
        if str.isupper(x):
            up += 1
    return up
ss = input()
print("Upper -", UpLow(ss))
print("Lower -", len(ss)- UpLow(ss))
