class transport():
    def __init__( self, brand, model ):
        self.brand = brand
        self.model = model
    def brnd(self):
        print(self.brand)

class cars(transport):
    def __init__(self, brand,model):
        #transport.__init__( self,brand,model )
        super().__init__(brand,model)
car = cars("Toyota", "Camry")
car.brnd()
'''x = input().split()
x1 = x[0]
x2 = x[1]
car2 = cars(x1,x2)
print( car.brand, car2.brand )
car.brnd()
'''
