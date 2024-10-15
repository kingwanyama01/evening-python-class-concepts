# Here we are going to use classes that we have defined to create objects
from my_classes import Car, Flower, Person, User, Admin

firstCar = Car("Subaru","SUV","2019","Ksh. 4M")
secondCar = Car("Toyota","Saloon","2017","Ksh. 1.8M")

print(firstCar.model)

firstFlower = Flower("Rose", "Ksh. 400")
secondFlower = Flower("Lily", "Ksh. 600")
thirdFlower = Flower("Sandy", "Ksh. 800")
fourthFlower = Flower("Orchid", "Ksh. 1200")
fifthFlower = Flower("Sunflower", "Ksh. 1500")
print(thirdFlower.price)

firstPerson = Person("Marvin","105","1.8 Mtrs")
secondPerson = Person("Jack","12","1.1 Mtrs")

print(secondPerson.run())

firstUser = User("Grace","N","gnjeri","Pa$$word!")
secondUser = User("Marvin","Irungu","mirungu","mI@123")

print(firstUser.register())

firstAdmin = Admin("X","Y","Z","P")
print(firstAdmin.login())
