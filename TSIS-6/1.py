def MaxOf3(x,y,z):
    if x > y > z or x > z > y:
        return x
    elif y > x > z or y > z > x:
        return y
    elif z > x > y or z > y > x:
        return z
    
a,b,c = map(int,input().split())
print(MaxOf3(a,b,c))