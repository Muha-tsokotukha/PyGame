lst = [word for line in open('input.txt') 
for word in line.split()]
print(*sorted(set(lst), key=lambda x: (-lst.count(x), x)),sep='\n')
