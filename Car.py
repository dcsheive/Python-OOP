class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print("Price:",self.price)
        print("Speed:",self.speed)
        print("Fuel:",self.fuel)
        print("Mileage:",self.mileage)
        print("Tax:",self.tax)
firstCar = Car(2000,"35mph","Full","20mpg")
secondCar = Car(20000,"55mph","Empty","15mpg")
firstCar.display_all()
secondCar.display_all()
