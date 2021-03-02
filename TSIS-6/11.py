def perf(a):
    summ = 1
    x = 2
    while x <= a:
        if a % x == 0:
            summ += x
        x += 1
    return summ/2 == a 
x = int(input())
print(perf(x))
