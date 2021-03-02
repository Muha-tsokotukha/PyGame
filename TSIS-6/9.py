from math import sqrt
def prime(a):
    x = 2
    while x <= sqrt(a):
        if a%x == 0:
            return False
        else: x += 1
    return True

n = int(input())
print(prime(n))
