x = input()
i = 0
for i in range(0, len(x)):
    if x[i] == 'G':
        print("G", end="")
        i +=1
    elif x[i] == '(':
        if x[i+1] == ')':
            print("o",end="")
            i = i + 2 
        else:
            print("al", end="")
            i = i + 3