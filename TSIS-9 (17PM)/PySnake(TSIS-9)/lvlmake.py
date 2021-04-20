'''
f = open('wallss.txt', 'w')
for x in range(1,25):
    for y in range(1,25):
        if x == 1 or x == 24 or y == 1 or y == 24:
            f.write('#')
        else: 
            f.write('.')
    f.write('\n')
'''
f = open('walls2.txt', 'w')
for x in range(1,25):
    for y in range(1,25):
        if x == 1 and y in range(1,6) :
            f.write('#')
        elif x == 24 and y in range(1,6):
            f.write('#')
        elif x == 1 and y in range(18,25):
            f.write('#')
        elif x == 24 and y in range(18,25):
            f.write('#')
        elif y == 1 and x in range(1,6):
            f.write('#')
        elif y == 24 and x in range(1,6):
            f.write('#')
        elif y == 1 and x in range(18,25):
            f.write('#')
        elif y == 24 and x in range(18,25):
            f.write('#')
         
        else: 
            f.write('.')
    f.write('\n')
    