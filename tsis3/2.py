a = input().split()
mn = 1e9
i = 0
for i in range(len(a)):
    b = int( a[i] )
    if mn > b and b > 0:
        mn = b
print(mn) 