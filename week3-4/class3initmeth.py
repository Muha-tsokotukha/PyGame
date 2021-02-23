class car():
    def __init__(self,  brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def findnt(self):
        print( self.brand +" is far better than" ,end=" ")    
car1 = car(input(), input(), int(input()))
avaiable = car( "BMW", "3", 1000000 ) 
if car1.brand == avaiable.brand and car1.model == avaiable.model and car1.price >= avaiable.price :
    print(avaiable.price)
else : 
    avaiable.findnt()
    print(car1.brand) 

