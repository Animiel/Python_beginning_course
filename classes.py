######################

# classes and objects



class Vehicle:
    def __init__(self, make, model):
        self.make = make            # self represents the object created
        self.model = model
    def moves(self):            # properties are details about the object (ex: model, tires, price) and methods are actions the object can take (ex: moving)
        print("Moves along...")
    
    def getMakeModel(self):
        print(f"I'm a {self.make} {self.model}.")

myCar = Vehicle("Clio", "4")
# print(myCar.make)
# print(myCar.model)
myCar.getMakeModel()
myCar.moves()

car2 = Vehicle("Volkswagen", "Polo 3")
car2.getMakeModel()
car2.moves()



##################

# inheritance



class Airplane(Vehicle):
    def __init__(self, make, model, faaId):
        super().__init__(make, model)           # inherit from parent
        self.faaId = faaId

    def moves(self):
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass            # inherits everything => no overriding

cessna = Airplane("Cessna", "Skyhawk", "N-12345")
mack = Truck("Mack", "Pinnacle")
golfKart = GolfCart("Golf", "Kart")

cessna.getMakeModel()
print(cessna.faaId)
cessna.moves()
mack.getMakeModel()
mack.moves()
golfKart.getMakeModel()
golfKart.moves()

print("\n\n")



#####################

# polymorphism



for v in (myCar, car2, cessna, mack, golfKart):
    v.getMakeModel()
    v.moves()
