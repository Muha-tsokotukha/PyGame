x = int(input())
prod = 1
symma = 0
while x > 0:
    prod *= x%10
    symma += x%10
    x //= 10
print( abs(prod - symma) )