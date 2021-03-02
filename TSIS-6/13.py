def Pasc(n):  
  
    for line in range(1, n + 1):  
        a = 1

        for i in range(1, line + 1):  
              
            print(a, end = " ")
            a = int(a * (line - i) / i)  
        print("")  
    

Pasc(int(input())) 