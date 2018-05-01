class Store:
    def __init__(self, location, owner):
        self.location = location
        self.owner = owner
        self.products = []
    def addProduct(self,price,name,weight,brand):
        self.products.append([price,name,weight,brand])
        return self
    def removeProduct(self, name):
        for i in range(0,len(self.products)):
            for j in range(0,len(self.products)):
                if self.products[i][j] == name:
                    del self.products[i]
                    return self
    def inventory(self):
        for i in range(0,len(self.products)):
            print("Product", (i + 1))
            for j in range(0,len(self.products[i])):
                print(self.products[i][j])
            print()
        print()
myStore = Store('14567 Willard Way', 'Jon')
myStore.addProduct(400, 'Purse', '5kg', 'Dolce & Gabbana')
myStore.inventory()
myStore.addProduct(200, 'Shoes', '7kg', 'Air Jordans')
myStore.addProduct(100, 'Toothbrush', '4kg', 'Gucci')
myStore.addProduct(700000, 'Car', '4000kg', 'Lamborghini')
myStore.inventory()
myStore.removeProduct('Purse')
myStore.inventory()