def rev(a):
    strrev = ""
    mass = len(a) - 1
    while mass >= 0:
        strrev += a[mass]
        mass -= 1
    return strrev
st = input()
print(rev(st))