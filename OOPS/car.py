class Car:
    ludo = "classiamhehehehhahhaha"
    counter = 0
    def __init__(self, model, cost, color):
        self.model = model
        self.cost = cost
        self.color = color
        Car.counter += 1
        
    def __repr__(self):
        return f"Car(model={self.model}, cost={self.cost})"
    def drive(self):
        print (f" You drive {self.color} {self.model}")


class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
        print (f"Created an animal of species: {self.species}, age: {self.age}")
    
    def eating(self):
        print (f"The {self.species} is eating.")
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class fish(Animal):
    pass

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw (self, amount):
        
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
            print(f"your new balance after withdrawing {amount} is : {self.balance}")
    def deposit (ramesh, amount):
        ramesh.balance += amount
        print("deposit successful")

class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def reads (self):
        print(f"reading {self.title} ")
