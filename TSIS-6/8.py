def unique(arr):
    uni = set(arr)
    return uni

arr = list(map(int, input().split()))

print(*unique(arr))