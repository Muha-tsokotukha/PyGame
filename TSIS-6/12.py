def ispal(x):
    i = 0
    for i in range(0, (len(x)//2)):
        if x[i] != x[len(x)-i-1]:
            return False
    return True
word = input()
print(ispal(word))