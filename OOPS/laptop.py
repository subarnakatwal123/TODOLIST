class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
    
    def increase_ram(self, increaseram):
        self.ram += increaseram
        print(f"ram upgraded successfully. New RAM on {self.brand} is {self.ram}")

    def increasestorage(self, increasestorage):
        self.storage += increasestorage
        print(f"Storage upgraded successfully. New Storage on {self.brand} is {self.storage}")
    
    def showsepcs(self):
        print(f"Brand : {self.brand} \n RAM : {self.ram} \n Storage : {self.storage}")
    

class Computer(Laptop):
    def __init__(self, brand, ram, storage, graphics):
        super().__init__( brand, ram, storage)
        self.graphics = graphics
        print(f"you have successfully installed {self.graphics}")

    def showsepcs(self):
        super().showsepcs()
        print(f"Graphics : {self.graphics}")

class digitial (Computer):
    def __init__ (self, brand, ram, graphics):
        super().__init__(brand, ram, graphics)
        print("{self.brand} {self.graphics} {self.ram}")