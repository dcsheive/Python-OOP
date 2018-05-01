class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print('Price:',self.price,'Max Speed:',self.max_speed,"Miles:",self.miles)
    def ride(self):
        print('Riding')
        self.miles += 10
        return self
    def reverse(self):
        if not(self.miles < 5):
            print('Reversing')
            self.miles -= 5
            return self
        return self
firstBike = Bike('$200',"25mph")
secondBike = Bike('$150',"23mph")
thirdBike = Bike('$190',"24mph")
firstBike.ride().ride().ride().reverse().displayInfo()
secondBike.ride().ride().reverse().reverse().displayInfo()
thirdBike.reverse().reverse().reverse().displayInfo()

