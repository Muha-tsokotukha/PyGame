arr = input().split()
i = 0
cnt = 0
for i in range( len(arr) ) :
    if arr[i] != '0':
        print( arr[i], end=" " )
    else : cnt += 1
while cnt > 0:
    print(0, end = " ")
    cnt -= 1