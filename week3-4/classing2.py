class transport():
    def __init__( self, brand, model ):
        self.brand = brand
        self.model = model
    def brnd(self):
        print(self.brand)
    
class cars(transport):
    def __init__(self, brand,model,price):
        super().__init__(brand,model)
        self.price = price
    def prs(self):
        print(self.price*2)


car = cars("Toyota", "Camry", int(input()))
car.prs()
car.brnd()

