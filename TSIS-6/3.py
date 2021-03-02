def product(a):
    prod  = 1
    for elem in a:
        prod *= elem
    return prod

arr = list(map(int, input().split()))
print(product(arr))