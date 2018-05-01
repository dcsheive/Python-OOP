class Animal:
    def __init__(self, name):
        self.health = 100
        self.name = name
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print('Health of', self.name, "is", self.health)
        return self
firstAnimal = Animal('Freddy')
firstAnimal.displayHealth()
firstAnimal.walk().walk().walk().run().run().displayHealth()
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.name = name
    def pet(self):
        self.health += 5
        return self
firstDog = Dog('Joe')
firstDog.walk().walk().walk().run().run().pet().displayHealth()
class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170
        self.name = name
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        super().displayHealth()
        print('I am a Dragon')
firstDragon = Dragon('Jeff')
firstDragon.run().fly().displayHealth()
firstDog.pet().pet().walk().pet().run().displayHealth()
firstDragon.fly().fly().displayHealth()