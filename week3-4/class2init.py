class car():
    def __init__(self,  brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
car1 = car(input(), input(), int(input()))
aviable = car( "BMW", "3", 1000000 ) 
if car1.brand == aviable.brand and car1.model == aviable.model and car1.price >= aviable.price :
    print(aviable.price)
else : print("Not found")
