def sumArr(a):
    summa = 0
    for element in a:
        summa += element
    return summa

arr = list(map(int, input().split()))

print(sumArr(arr))
