class Product:
    def __init__(self,price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def addTax(self, tax):
        self.price = self.price + (self.price * tax)
        return self.price
    def Return(self,reason):
        if reason == 'defective':
            self.status = 'Defective'
            self.price = 0
        elif reason == 'like new':
            self.status = 'For Sale'
        elif reason == 'opened':
            self.status = 'Used'
            self.price = self.price * .8
        else:
            return 'incorrect reason'
        return self
    def displayInfo(self):
        print("Status:", self.status)
        print("Name:", self.name)
        print("Brand:",self.brand)
        print("Weight:",self.weight)
        print("Price:", self.price)
        print()
firstProduct = Product(400, 'Purse', '5kg', 'Dolce & Gabbana')
secondProduct = Product(200, 'Shoes', '7kg', 'Air Jordans')
thirdProduct = Product(100, 'Toothbrush', '4kg', 'Gucci')
fourthProduct = Product(700000, 'Car', '4000kg', 'Lamborghini')
firstProduct.displayInfo()
secondProduct.displayInfo()
thirdProduct.displayInfo()
fourthProduct.displayInfo()
firstProduct.sell().addTax(.03)
firstProduct.displayInfo()
firstProduct.Return('defective')
firstProduct.displayInfo()
secondProduct.Return('opened')
secondProduct.displayInfo()
thirdProduct.Return('like new')
thirdProduct.displayInfo()