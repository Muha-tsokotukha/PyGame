f = open('1.txt', 'w')
f2 = open('2.txt', 'w')
f3 = open('3.txt', 'w')

for i in range(0, 600):
    for j in range(0,800):
        if i == 100 and (j in range( 30,500 )):
            f.write('#')
            continue    
        f.write('.')
    f.write('\n')


for i in range(0, 600):
    for j in range(0,800):
        if i == 450 and (j in range( 30,500 )):
            f2.write('#') 
            continue
        if j == 50 and (i in range( 100,400 )):
            f2.write('#')
            continue    
        if j == 620 and (i in range(300, 500)):
            f2.write('#')
            continue
        if i == 150 and (j in range(400, 600)):
            f2.write('#')
            continue
        f2.write('.')
    f2.write('\n')

for i in range(0, 600):
    for j in range(0,800):
        if i == 450 and (j in range( 30,500 )):
            f3.write('#') 
            continue
        if i == 50 and (j in range( 30,500 )):
            f3.write('#')
            continue    
        f3.write('.')
    f3.write('\n')
