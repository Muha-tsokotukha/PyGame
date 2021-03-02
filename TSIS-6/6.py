def numInRange(a,l,r):
    return l<=a<=r
x,y,z = map(int, input().split())
print(numInRange(x,y,z))