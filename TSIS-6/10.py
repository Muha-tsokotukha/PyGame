def arrEven(ar):
    for x in ar:
        if x % 2 == 0:
            print(x, end=" ")
arr = list(map(int, input().split()))
arrEven(arr)