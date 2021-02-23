qw = input().split()
n = int(qw[0])  
m = int(qw[1])  
bor = {'#'}
anya = {'$'}
while n > 0:
    bor.add(int(input()))
    n -= 1
while m > 0:
    anya.add(int(input()))
    m -= 1
bor.remove('#')
anya.remove('$')
sec = bor.intersection(anya)
print(len(sec))
print(*sec)

print(len(bor.difference(anya)))
print(*sorted(bor.difference(anya)))  

print(len(anya.difference(bor)))
print(*sorted(anya.difference(bor)))