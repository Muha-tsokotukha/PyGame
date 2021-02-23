a = input().split()
k = int(input())
k = k % len(a)
if k<0:
    k = abs(k)
    print(*a[k:],end =" " )
    print(*a[0:k])
elif k>=0:
    k = abs(k)
    print(*a[-k:],end =" ")
    print(*a[0:-k])
"""
1 2 3 4 5 6 7 
5 6 7 1 2 3 4 n - k
"""